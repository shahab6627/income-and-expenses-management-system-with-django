 
    // getting all model inputFields 
    const modal_expenseInput = document.getElementById('expense')
    const modal_expenseAmountInput = document.getElementById('amount')
    const modal_descriptionInput = document.getElementById('description')
    const modal_expenseCategoryInput = document.getElementById('expense_cat')
    const modal_expenseDateInput = document.getElementById('date')
    const modal_expenseIdInput = document.getElementById('expense_id')

    // getting specific record data to be updated 
    const update_expense = [...document.getElementsByClassName('edit-expense')]
    update_expense.forEach(update_expense=>update_expense.addEventListener('click', ()=>{
        var expense = update_expense.getAttribute('data-expense')
        var expense_amount = update_expense.getAttribute('data-amount')
        var expense_description = update_expense.getAttribute('data-description')
        var expense_category = update_expense.getAttribute('data-expense-cat')
        var expense_category_value = update_expense.getAttribute('data-expense-cat-id')
        var expense_date = update_expense.getAttribute('data-date')
        var expense_id = update_expense.getAttribute('data-expense-id')


        modal_expenseInput.value = expense
        modal_descriptionInput.value = expense_description
        modal_expenseAmountInput.value = expense_amount
        modal_expenseIdInput.value = expense_id


        var option = document.createElement('option');
        option.innerHTML = expense_category
        option.value = expense_category_value
        option.setAttribute('selected', true);
        modal_expenseCategoryInput.remove(option)

        modal_expenseCategoryInput.prepend(option)

        // modal_expenseDateInput.value(expense_date)
        

    }))



// delete an expense 
    var expense = [...document.getElementsByClassName('delete-expense')]
    expense.forEach(expense=>expense.addEventListener('click', ()=>{
        var conf = confirm("agree..!")
        if(conf == true){
        const expense_id = expense.getAttribute('data-expense-id')

        fetch(`delete-expense/${expense_id}`, {
            // body:JSON.stringify({expense_id : expense_id}),
            method :"GET",

        }).then((res)=>res.json())
        .then((data)=>{
            if(data.success){
                var expense_row = document.getElementById(`tr-${expense_id}`)
                expense_row.remove()
                console.log(data.success);
                console.log(data.expense);
            }else{
                console.log(data.error);
            }
        })
    }else{
        console.log(conf);
    }

    }))



const edit_income_btn = [...document.getElementsByClassName('edit-income')]

edit_income_btn.forEach(edit_income_btn=>edit_income_btn.addEventListener('click', ()=>{
    var income = edit_income_btn.getAttribute('data-income')
    var income_source = edit_income_btn.getAttribute('data-income-source')
    var amount = edit_income_btn.getAttribute('data-amount')
    var description = edit_income_btn.getAttribute('data-description')
    var income_id = edit_income_btn.getAttribute('data-income-id')
    console.log(income_source);

    document.getElementById('income').value = income
    var income_source_filed = document.getElementById('income_source')
    document.getElementById('amount').value = amount 
    document.getElementById('income_id').value = income_id 
    document.getElementById('description').value = description

    var option = document.createElement('option')


    option.value = income_source 
    option.text = income_source
    option.setAttribute('selected', true)
    income_source_filed.remove(option)


    income_source_filed.append(option)


    

}))