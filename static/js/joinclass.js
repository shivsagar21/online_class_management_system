let target=document.getElementById("classinfo")

window.onload=()=>{
   let newcroom=localStorage.getItem("newINFO")
     let newdata=JSON.parse(newcroom)
      console.log(newdata);
     let div=document.createElement("div");
    div.setAttribute("class","card")
    let image=document.createElement("img")
    image.src=newdata[1];
    image.setAttribute("class","cardimage")
    
    let h2=document.createElement("h2")
    h2.textContent=newdata[2];
    
    let p=document.createElement("p")
    p.textContent=newdata[3];
    
    let button=document.createElement("button");
    let a=document.createElement("a");
    a.href=newdata[4];
    a.textContent="Join Class"
    
    button.appendChild(a);
    
    div.appendChild(image);
    div.appendChild(h2);
    div.appendChild(p);
    div.appendChild(button);
    console.log(div.innerHTML);

   target.insertBefore(div,target.children[0])
}