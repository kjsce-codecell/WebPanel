function search(){
    var name=document.getElementById('searchitem').value.toUpperCase();
    var table=document.getElementById('urls');
    var tr=table.getElementsByTagName("tr");
    for(var i=0;i<tr.length;i++){
        td=tr[i].getElementsByTagName("td")[0];
        if(td){
            if(td.innerHTML.toUpperCase().indexOf(name)>-1){
                tr[i].style.display="";
            }else{
                tr[i].style.display="none";
            }
        }
    }
}
