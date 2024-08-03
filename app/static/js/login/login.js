async function letHome (user, password) {
    await global.setSession(user, password)
    window.location.href = `${window.location.origin}/home`
}

async function verifyLogin ( user, password ) {
    if ( await login.login( user, password ) ) {
        letHome (user, password)
    }
}

document.querySelector(".login").onclick = () => {
    let user = document.querySelector(".login-usuario").value
    let password = document.querySelector(".login-senha").value

    verifyLogin(user, password)
} 

document.querySelector(".register").onclick = async () => {
    let email = document.querySelector(".register-email").value
    let cpf = document.querySelector(".register-cpf").value
    let user = document.querySelector(".register-usuario").value
    let pass1 = document.querySelector(".register-senha").value
    let pass2 = document.querySelector(".register-confirme-senha").value

    let res =  await register.register (email, user, cpf, pass1, pass2)
    if ( res === true ) {
        letHome (user, pass1)
    }
}

document.querySelector(".login-register").onclick = () =>{
    animation.login_to_register()
}

document.querySelector(".register-login").onclick = () =>{
    animation.register_to_login()
} 