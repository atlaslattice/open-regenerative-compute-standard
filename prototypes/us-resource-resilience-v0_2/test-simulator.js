const assert=require('node:assert/strict');const S=require('./simulator.js');
const row={annual_consumption:100,domestic_output_or_proxy:70,period:2025};
const a={years:30,recoveryCapacity:20,rampYears:5,initialStock:0,reserveFraction:.2,reserveBuildYears:1,stockLoss:.01,shockLoss:.5,shockYear:12,importCap:null,demandGrowth:0,productionGrowth:0};
const b=S.simulate(row,{...a,recoveryCapacity:0}),c=S.simulate(row,a);
for(const r of c.rows){assert.ok(Math.abs(r.production+r.recovery+r.imports+r.draw-r.served-r.addition-r.surplus)<1e-8);assert.ok(Math.abs(r.openingStock-r.loss-r.draw+r.addition-r.closingStock)<1e-8);assert.equal(r.actualExportAuthorization,false);assert.equal(r.unmet,0)}
assert.ok(c.rows.reduce((s,r)=>s+r.imports,0)<b.rows.reduce((s,r)=>s+r.imports,0));
assert.ok(c.rows[11].production<c.rows[10].production);
const shortage=S.simulate(row,{...a,years:1,initialStock:5,importCap:0,recoveryCapacity:0}).rows[0];assert.ok(shortage.unmet>0);assert.equal(shortage.exportCandidate,0);
assert.equal(S.simulate({...row,domestic_output_or_proxy:null},a).status,'UNKNOWN');
assert.throws(()=>S.simulate(row,{...a,initialStock:null}));assert.throws(()=>S.simulate(row,{...a,years:101}));
console.log('30-year mass/stock conservation, import comparison, disruption, shortages and UNKNOWN checks passed.');
