// Execute the embedded dashboard with a minimal DOM/canvas harness.
// This checks actual data/filter wiring; it is not a browser rendering test.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('outputs/dashboard.html','utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const elements={};
const ctx=new Proxy({}, {get:(o,k)=>o[k]||(()=>{}),set:(o,k,v)=>(o[k]=v,true)});
function element(id){return elements[id]||(elements[id]={value:'',innerHTML:'',textContent:'',clientWidth:1100,
 add(option){if(this.value==='')this.value=String(option.value)},addEventListener(){},
 getContext(){return ctx},getBoundingClientRect(){return {left:0}}});}
const sandbox={document:{getElementById:element},window:{devicePixelRatio:2,addEventListener(){}},
 Option:function(label,value){this.label=label;this.value=value},console};
vm.createContext(sandbox);vm.runInContext(script,sandbox);
assert.equal(vm.runInContext('filtered().length',sandbox),60);
element('price').value='price_pressure_500';vm.runInContext('draw()',sandbox);
assert.equal(vm.runInContext('filtered()[0].He3_price_USD_per_STP_L',sandbox),500);
element('offtake').value='He3_full_offtake_sensitivity';vm.runInContext('draw()',sandbox);
assert.equal(vm.runInContext('filtered()[0].He3_market_cap_STP_L_per_year_fleet',sandbox),null);
element('fleet').value='50';element('recovery').value='0.375';vm.runInContext('draw()',sandbox);
assert.equal(vm.runInContext('filtered().length',sandbox),60);
assert.equal(vm.runInContext('filtered()[0].fleet_modules',sandbox),50);
element('metric').value='actual_profit_USD';vm.runInContext('draw()',sandbox);
assert(element('detail').innerHTML.includes('UNRESOLVED'));
console.log('PASS: complete embedded data, four selector filters, DPR canvas path and unresolved-profit handling');
