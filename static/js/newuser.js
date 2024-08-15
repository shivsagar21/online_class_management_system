let date=new Date();
let s=new String(date)
document.querySelector("span").textContent=s.slice(0,-30);


document.getElementById("genotp").addEventListener("click",()=>{

  let ip=document.querySelectorAll(".uip")
  let arr=Array.from(ip);
 for(let a=0;a<arr.length;a++){
    if(arr[a].value==""){
        console.log(arr[a]);
        alert("Please fill all the field")
        return;
    } 
 }

  if(arr[1].value.length<6){
    alert("At least 6 digit password required")
    return;
  }

if(arr[1].value!=arr[2].value){
    alert("Both Confirm and New Password Should be same")
    return;
}


let v=document.querySelectorAll(".utype")

let arr1=Array.from(v);
if(!arr1[0].checked && !arr1[1].checked){
    alert("Please select Student or Instructor")
    return;
}




    document.getElementById("otp").classList.add("display")
})
