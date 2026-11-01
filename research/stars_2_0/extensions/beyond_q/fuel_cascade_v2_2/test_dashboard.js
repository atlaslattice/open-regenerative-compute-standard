// Minimal DOM/canvas execution harness, not a full browser rendering test.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const script=fs.readFileSync('outputs/dashboard.html','utf8').match(/<script>([\s\S]*?)<\/script>/)[1];
const elements={},context=new Proxy({}, {get:(o,k)=>o[k]||(()=>{}),set:(o,k,v)=>(o[k]=v,true)});
const element=id=>elements[id]||(elements[id]={value:'',innerHTML:'',textContent:'',clientWidth:1100,
 add(o){if(this.value==='')this.value=String(o.value)},addEventListener(){},getContext(){return context}});
const sandbox={document:{getElementById:element},window:{devicePixelRatio:2,addEventListener(){}},Option:function(label,value){this.label=label;this.value=value}};
vm.createContext(sandbox);vm.runInContext(script,sandbox);
assert.equal(vm.runInContext('filtered().length',sandbox),60);
element('scenario').value='eligible_pool';element('recovery').value='0.75';element('price').value='pressure_500';element('offtake').value='fleet_cap_stress';
vm.runInContext('draw()',sandbox);
assert.equal(vm.runInContext('filtered()[0].He3_price_USD_per_STP_L',sandbox),500);
assert.equal(vm.runInContext('filtered()[0].He3_retained_STP_L',sandbox),0);
assert.equal(vm.runInContext('filtered()[0].scenario',sandbox),'eligible_pool');
element('metric').value='actual_profit_USD';vm.runInContext('draw()',sandbox);
assert(element('detail').innerHTML.includes('UNRESOLVED'));
console.log('PASS: complete dashboard data, four scenario filters, zero retention, unresolved-profit rendering');
