

// show and hide password in input 
function toggleShowHidePassword(){
    var showHideText = document.getElementById('toggleShowHidePassword')
 
    var passwordField = document.getElementById('password')
    if(showHideText.textContent === "show"){
        showHideText.textContent = "hide"
        passwordField.setAttribute('type','text')
    }else{
        showHideText.textContent = "show"
        passwordField.setAttribute('type','password')
    }
}
function toggleShowHideRePassword(){
    // show and hide password in repeat password field 
    var showHideRepeatPassword = document.getElementById('toggleShowRepeatHidePassword')
    
    var repeatPasswordField = document.getElementById('r_password')
    if(showHideRepeatPassword.textContent === "show"){
        showHideRepeatPassword.textContent = "hide"
        repeatPasswordField.setAttribute('type','text')
    }else{
        showHideRepeatPassword.textContent = "show"
        repeatPasswordField.setAttribute('type','password')
    }
}


// validating username from server 
function validateUsername(){

var username = document.getElementById("username")
const usernameValue = username.value
if (usernameValue.length>0){
    fetch(
        "validate-username",{
            body:JSON.stringify({username:usernameValue}),
            method:"POST",

        }).then((res)=>res.json())
        .then((data) => { 
            console.log(data);
            if(data.username_error){
                console.log("username error");
                username.classList.add('is-invalid')
                document.getElementById('username-error').innerHTML = `${data.username_error}`
                document.getElementById('register-btn').disabled = true;
            }
            else{
                console.log(data.success);
                username.classList.remove('is-invalid')

                username.classList.add('is-valid')
                document.getElementById('username-error').innerHTML = ``
                document.getElementById('register-btn').disabled = false;


            }
        })
    }
    else{
        username.classList.add('is-invalid')
        document.getElementById('username-error').innerHTML = 'username is required'
        document.getElementById('register-btn').disabled = true
    }
    }



    // validating email from server
    function validateEmail(){
        var user_email = document.getElementById('email')
        const user_email_value = user_email.value
        if(user_email_value.length>0){

        fetch('validate-email', {
            body: JSON.stringify({user_email : user_email_value}),
            method:'POST'

        }).then((res)=>res.json())
        .then((data)=>{
            if(data.email_error){
                user_email.classList.add('is-invalid')
                document.getElementById('email_error').innerHTML = `${data.email_error}`
                document.getElementById('register-btn').disabled=true
            }
            else{
                console.log(data.success);
                user_email.classList.remove('is-invalid')
                document.getElementById('email_error').innerHTML = ``
                user_email.classList.add('is-valid')
                document.getElementById('register-btn').disabled=false


            }
        })
    }
    else{
        user_email.classList.add('is-invalid')
        document.getElementById('email_error').innerHTML = 'email is required'
        document.getElementById('register-btn').disabled=true

    }
    }

function createUser(){
    var username = document.getElementById('username')
    const username_value = username.value
    var email = document.getElementById('email')
    const email_value = email.value
    var password = document.getElementById('password') 
    const password_value = password.value
    var r_password = document.getElementById('r_password')
    const r_password_value = r_password.value


    // checking for empty fields 
    if(username_value == ""){
        username.classList.add('is-invalid')
        document.getElementById('username_error').innerHTML = 'username is required'
        return
    }
    else if (email_value == ""){
        email.classList.add('is-invalid')
        document.getElementById('email_error').innerHTML = 'email is required'
        return
    }
    else if (password_value == ""){
        password.classList.add('is-invalid')
        document.getElementById('password_error').innerHTML = 'password is required'
        return
    }
    else if (r_password_value == ""){
        r_password.classList.add('is-invalid')
        document.getElementById('r_password_error').innerHTML = 'repeat password is required'
        return
    }else{

        document.getElementById('register-span').classList.remove('displayNone')
        fetch('/',{
            body: JSON.stringify({
                username : username_value,
                email : email_value,
                password : password_value
            }
            ),
            method:"POST"
        }).then((res)=>res.json())
        .then((data)=>{
            if(data.success){
                document.getElementById('register-span').classList.add('displayNone')

                document.getElementById('register-form').reset()
                document.getElementById('success-msg').innerHTML = `<div class="alert alert-success alert-dismissible fade show" role="alert">
                ${data.success}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>`
            }
        })
    }
   
}

// checking weather passwords matching or not 

function checkPasswords(){
    var _password = document.getElementById('password')
    var repeat_password = document.getElementById('r_password')

    document.getElementById('r_password_error').innerHTML = ''
    repeat_password.classList.remove('is-invalid')

    if (repeat_password.value != _password.value){
        repeat_password.classList.add('is-invalid')
        document.getElementById('r_password_error').innerHTML = 'passwords are not matching'
        document.getElementById('register-btn').disabled=true

        
    }else{
        repeat_password.classList.add('is-valid')
        document.getElementById('r_password_error').innerHTML = ''
        document.getElementById('register-btn').disabled=false
    }
}



// login user 

function loginUser(){
    var username = document.querySelector('#username').value
    var password = document.querySelector('#password').value
    // checking if input fields are empty 
    if(username == ""){
        document.getElementById('username_error').innerHTML = "username is required"
        return
    }
    else if(password == ""){
        document.querySelector('#password_error').innerHTML = "password is required" 

    }else{

        fetch('login', {
            body : JSON.stringify({username : username, password : password}),
            method:"POST"
        }).then((res)=>res.json())
        .then((data)=>{
            if(data.login_error){
                document.getElementById('login-alert').classList.remove('displayNone')
            }else{
                location.href = `http://localhost:8000/profile/${data.username}`;
            }
            
        })
    }
}

// remove error messages by keyup on input fields 
function removeUsernameError(){
    document.querySelector('#username_error').innerHTML = "" 

}
function removePasswordError(){
    document.querySelector('#password_error').innerHTML = "" 

}

// show and hide password 

function toggleShowHideLoginPassword(){
    var toggle_value = document.querySelector('#showhidePassword')
    var passwordInput = document.querySelector('#password')
    if(toggle_value.textContent === 'show'){
        toggle_value.textContent = "hide"
        passwordInput.setAttribute('type','text')

    }else{
        toggle_value.textContent = 'show'
        passwordInput.setAttribute('type','password')
    }
}


// send reset password email 

function sendResetPasswordMail(){

    var emailInput = $("#email").val()
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    var csrf_val= csrf[0].value
    console.log(csrf_val);

    $.ajax({
        url : 'reset-password-send-mail',
        type:"POST",
        data:{
            'csrfmiddlewaretoken':csrf_val,
            'email':emailInput
        },
        success: function(res){
            console.log(res);
        },
        error: function(error){
            console.log(error);
        }
    })
    }

// reset password 
function resetPassword(){
    const password = document.querySelector('#password').value 
    const r_password = document.querySelector('#r_password').value 


    if (password ==""){
        document.getElementById('password_error').textContent="password is required"
        return
    }
    else if(r_password == ""){
        document.getElementById('r_password_error').textContent = "repeat password is required"
        document.getElementById('password_error').textContent=""

        return
    }
    else if(password != r_password){
        document.getElementById('r_password_error').textContent = "passwords are not matching"
        return
    }
}
