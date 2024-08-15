let back=document.getElementById("back")
let opt=document.getElementById("option")
let upd=document.getElementById("update");
document.getElementById("dropdown").addEventListener("click",()=>{
   opt.classList.toggle("show")
})
back.addEventListener("click",()=>{
    opt.classList.remove("show")
})

document.querySelector(".profile").addEventListener("click",()=>{
    upd.classList.toggle("display")
})






