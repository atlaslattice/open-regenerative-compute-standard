// Node standard-library logic check. This is NOT browser rendering/layout QA.
const fs=require('fs'),vm=require('vm'),path=require('path');
const html=fs.readFileSync(path.join(__dirname,'../outputs/dashboard.html'),'utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
new vm.Script(script);
for(const width of [360,1000]){
 class E {
  constructor(id){this.id=id;this.value=id==='case'?'A1':id==='metric'?'total_inventory':'0';this.clientWidth=width;this.children=[];this.attrs={};this.handlers={};}
  setAttribute(k,v){this.attrs[k]=v;}
  appendChild(e){this.children.push(e);}
  replaceChildren(){this.children=[];}
  addEventListener(k,v){this.handlers[k]=v;}
 }
 const nodes=Object.fromEntries(['case','metric','day','plot','dayLabel','detail','download'].map(id=>[id,new E(id)]));
 const context={document:{getElementById:id=>nodes[id],createElementNS:()=>new E(),createElement:()=>new E()},ResizeObserver:class{constructor(cb){this.cb=cb;}observe(){this.cb();}},console,setTimeout,Blob,URL};
 vm.runInNewContext(script,context);
 for(const selected of ['A0','A1','A2']){
  nodes.case.value=selected;nodes.case.handlers.input();
  for(const metric of ['total_inventory','b_store','b_unserved_burn']){
   nodes.metric.value=metric;nodes.metric.handlers.input();
   nodes.day.value=nodes.day.max;nodes.day.handlers.input();
   if(!nodes.detail.textContent.includes(selected))throw Error('case interaction failed');
   if(nodes.plot.children.some(e=>Object.values(e.attrs).some(v=>String(v).includes('NaN'))))throw Error('invalid chart coordinates');
  }
 }
 console.log(JSON.stringify({width,caseMetricInteractions:9,validCoordinates:true,mode:'DOM logic check only; rendered-browser QA unavailable'}));
}
