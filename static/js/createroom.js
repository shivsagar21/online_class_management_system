
let inputs=document.querySelectorAll("input")
let inputarr=Array.from(inputs)
let msg=document.getElementById("successmessage")
let newdata=[];
document.getElementById("createnew").addEventListener("click",()=>{
    newdata.splice(0,newdata.length)
    inputarr.forEach((data)=>{
      newdata.push(data.value)
    })
  
   let v=JSON.stringify(newdata);

   localStorage.setItem("newINFO",v)

   msg.style.display="block"
   setTimeout(()=>{
    msg.style.display="none"
   
  },1500)
    
})







