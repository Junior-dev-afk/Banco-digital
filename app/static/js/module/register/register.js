class Register {
    constructor(){}

    async register (email, user, cpf, pass1, pass2) {
        let response = await fetch("/getRegister", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({email : email, user : user, cpf : cpf, pass1 : pass1, pass2 : pass2})
        })

        if ( !response.ok ) {
            throw new Error("Problema ao registrar usuario")
        }

        let data = await response.json()

        if ( data.response != true ) {
            global.notify(data.response)
            return false
        }

        return true
    }
}


const register = new Register()