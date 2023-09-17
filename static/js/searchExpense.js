var total_amount_span =  document.getElementById('total-amount')

const total_amount_value= total_amount_span.innerHTML

function searchExpense(){
    var search_exp = document.querySelector('#searchExp').value 
                    
    if(search_exp.length>0){
    fetch(
        `search-expense/${search_exp}`,{
            method:"GET",

        }).then((res)=>res.json())
        .then((data) => { 
            if(data.length === 0){
                console.log(data);
                document.getElementById('search-table-body').innerHTML="no result found"
                total_amount_span.innerHTML=0


            }else{
                document.getElementById('expense-table').classList.add('displayNone')
                document.getElementById('search-result').classList.remove('displayNone')
                const tbody = document.getElementById('search-table-body')
                tbody.innerHTML =``
                amount = 0
                data.forEach((element,index) => {
                    amount+=element.amount
                    console.log(amount)

                    tbody.innerHTML +=`
                    <tr>
                    <td>${index}</td>
                    <td>${element.expense}</td>
                    <td>${element.amount}</td>
                    <td>${element.description}</td>
                    <td>${element.date}</td>
                    </tr>
                    `
                    total_amount_span.innerHTML=amount
                });

            }
         
    })
}else{
    document.getElementById('expense-table').classList.remove('displayNone')
    document.getElementById('search-result').classList.add('displayNone')
    total_amount_span.innerHTML=total_amount_value
    console.log(total_amount_value);




}
}