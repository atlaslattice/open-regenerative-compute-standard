/* US prototype calculation module. All results are screening/simulation only. */
const USLedger = (() => {
 const finite = v => typeof v === 'number' && Number.isFinite(v) && v >= 0;
 function calculate(row,extra=0,reserve=null,reservePct=.2,buildYears=1) {
  if(!finite(extra)||!finite(reservePct)||!finite(buildYears)||buildYears===0||
     (reserve!==null&&!finite(reserve))) throw Error('Invalid scenario input');
  const c=row.annual_consumption,p=row.domestic_output_or_proxy;
  const target=finite(c)?c*reservePct:null;
  const supply=finite(p)?p+extra:null;
  const productionGap=finite(c)&&supply!==null?Math.max(c-supply,0):null;
  const reserveGap=target!==null&&reserve!==null?Math.max(target-reserve,0):null;
  const importsNeeded=finite(c)&&supply!==null&&reserveGap!==null?
    Math.max(c+reserveGap/buildYears-supply,0):null;
  const exportCandidate=finite(c)&&supply!==null&&target!==null&&reserve!==null?
    (reserve>=target?Math.max(supply-c,0):0):null;
  return {target,supply,productionGap,reserveGap,importsNeeded,exportCandidate,
    authority:'NONE',actualExportAuthorization:false,status:'SIMULATED / PROXY'};
 }
 function selectRows(rows,state='',county='') {
  return rows.filter(r=>state?(r.geo_level!=='national'&&r.state_fips===state&&
    (county?r.county_fips===county:r.geo_level==='state')):r.geo_level==='national');
 }
 function validateRegional(rows) {
  if(!Array.isArray(rows)||rows.length>10000)throw Error('Expected at most 10,000 rows');
  return rows.map(r=>{
   if(!r||!['state','county'].includes(r.geo_level)||typeof r.id!=='string'||typeof r.unit!=='string'||
    !/^\d{2}$/.test(r.state_fips)||r.geo_level==='county'&&(!/^\d{5}$/.test(r.county_fips)||!r.county_fips.startsWith(r.state_fips)))
      throw Error('Every regional record needs a material, unit and matching FIPS');
   for(const k of ['annual_consumption','domestic_output_or_proxy'])
    if(r[k]!==null&&!finite(r[k]))throw Error('Use finite nonnegative numbers or null');
   return {...r,evidence_status:'LOCAL IMPORT / UNVERIFIED'};
  });
 }
 return {calculate,selectRows,validateRegional};
})();
if(typeof module!=='undefined')module.exports=USLedger;
