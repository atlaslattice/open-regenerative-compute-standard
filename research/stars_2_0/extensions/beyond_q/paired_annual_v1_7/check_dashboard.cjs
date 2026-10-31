// Functional DOM/canvas smoke test, not visual browser qualification.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(__dirname+'/dashboard.html','utf8');
const js=html.split('<script>')[1].split('</script>')[0];
const context2d=new Proxy({}, {get:(o,k)=>o[k]||(()=>{}),set:(o,k,v)=>(o[k]=v,true)});
const nodes={};
function node(id){return nodes[id]||(nodes[id]={value:'',options:[],innerHTML:'',textContent:'',appendChild(o){this.options.push(o);if(!this.value)this.value=o.value;},getContext(){return context2d;}});}
const context={document:{getElementById:node,createElement:()=>({value:'',textContent:''})}};
vm.createContext(context);vm.runInContext(js,context,{timeout:5000});
let count=0;
for(const a of node('config').options)for(const b of node('blanket').options)for(const s of node('schedule').options){
 node('config').value=a.value;node('blanket').value=b.value;node('schedule').value=s.value;
 vm.runInContext('draw()',context,{timeout:5000});
 assert(node('status').textContent.includes('tritium'));assert(node('energy').innerHTML.includes('UNRESOLVED')||node('energy').innerHTML.includes('gain'));
 count++;
}
console.log('Dashboard JS syntax and '+count+' selection combinations pass with mocked DOM/canvas.');
