class Login {
    constructor(){}


     async login ( user, password) {
        let response = await fetch( "/verifyLogin", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({'user' : user, 'password' : password})
        } )

        if ( !response.ok ) {
            throw new Error( "Falha ao solicitar login" )
        }

        let data = await response.json()

        if ( !data.response ) {
            global.notify("Usuario ou senha incorreta")
        }

        return data.response
    }

}

const login = new Login()