/* Annual national material-flow sensitivity engine. No empirical-impact or export authority. */
const USSimulator=(()=>{
 const n=x=>typeof x==='number'&&Number.isFinite(x)&&x>=0;
 function simulate(row,a){
  if(!n(row.annual_consumption)||!n(row.domestic_output_or_proxy))return {status:'UNKNOWN',rows:[],reason:'Missing physical baseline'};
  const keys=['years','recoveryCapacity','rampYears','initialStock','reserveFraction','reserveBuildYears','stockLoss','shockLoss','shockYear'];
  for(const k of keys)if(!n(a[k]))throw Error('Missing/invalid assumption: '+k);
  if(!Number.isInteger(a.shockYear)||a.shockYear>100)throw Error('Invalid shock year');
  if(!Number.isInteger(a.years)||a.years<1||a.years>100||a.rampYears<1||a.reserveBuildYears<1||a.stockLoss>1||a.shockLoss>1)throw Error('Invalid horizon, ramp or loss fraction');
  for(const k of ['demandGrowth','productionGrowth'])if(!Number.isFinite(a[k])||a[k]<=-1||a[k]>1)throw Error('Invalid growth rate');
  if(a.importCap!==null&&!n(a.importCap))throw Error('Invalid annual import cap');
  let stock=a.initialStock;const rows=[];
  for(let t=1;t<=a.years;t++){
   const demand=row.annual_consumption*(1+a.demandGrowth)**t;
   const normalProduction=row.domestic_output_or_proxy*(1+a.productionGrowth)**t;
   const disruption=t===a.shockYear?a.shockLoss:0;
   const production=normalProduction*(1-disruption);
   const recovery=a.recoveryCapacity*Math.min(t/a.rampYears,1)*(1-disruption);
   const openingStock=stock,loss=stock*a.stockLoss;stock-=loss;
   const target=demand*a.reserveFraction;
   const desiredAddition=Math.max(target-stock,0)/a.reserveBuildYears;
   const importsRequested=Math.max(demand+desiredAddition-production-recovery,0);
   const imports=a.importCap===null?importsRequested:Math.min(importsRequested,a.importCap);
   let available=production+recovery+imports;
   const draw=Math.min(stock,Math.max(demand-available,0));stock-=draw;available+=draw;
   const served=Math.min(demand,available),unmet=demand-served;
   const addition=Math.min(Math.max(target-stock,0),Math.max(available-served,0));stock+=addition;
   const surplus=Math.max(available-served-addition,0);
   const exportCandidate=unmet<1e-9&&stock+1e-9>=target?surplus:0;
   rows.push({year:(Number.isInteger(row.period)?row.period:2025)+t,demand,production,recovery,openingStock,loss,importsRequested,imports,draw,served,unmet,addition,closingStock:stock,reserveTarget:target,surplus,exportCandidate,actualExportAuthorization:false});
  }
  return {status:'SIMULATED / UNCALIBRATED',rows};
 }
 return {simulate};
})();
if(typeof module!=='undefined')module.exports=USSimulator;
