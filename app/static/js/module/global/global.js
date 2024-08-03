class Global {
    constructor () {
        this.noti = false
        this.noti_timeout = false
        this.saldo = false
    }

    async setSession ( user, password ) {
        let response = await fetch("/setSession", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({user : user, password : password})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao verificar sessao")
        }

        let data = await response.json()

        if ( data.response ) {
            sessionStorage.setItem("user", user)
            sessionStorage.setItem("password", password)
        }
    }

    async getSession ( ) {

        let user = sessionStorage.getItem("user")
        let password = sessionStorage.getItem("password")

        let response = await fetch("/setSession", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({user : user, password : password})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao verificar sessao")
        }

        let data = await response.json()

        if ( data.response ) {
            return sessionStorage.getItem("user")
        }

        return false
    }

    getPassword () {
        return sessionStorage.getItem("password")
    }

    async verifySession () {
        let session = await global.getSession()
    
        if ( session == false ){
            window.location.href = `${window.location.origin}/login`
        }

    }

    notify (msg) {
        let mens = document.createElement("div")
        mens.style.cssText = `
            font-size: 15px; 
            word-break: break-all; 
            padding: 20px; 
            border-radius: 10px; 
            z-index: 1; 
            position: fixed; 
            right: 10px; 
            top: 30px; 
            width: auto; 
            max-width: 300px; 
            height: auto; 
            background-color: rgb(0, 170, 57);
        `
        mens.innerHTML = msg
        if ( this.noti != false ) {
            this.noti.remove()
            clearTimeout(this.noti_timeout)
        }
        document.querySelector(".container").appendChild(mens)
        this.noti = mens
        setTimeout(()=>{
            mens.remove()
            this.noti = false
            this.noti_timeout = false
        }, 6000)
    }

    mostrarSaldo ( btn ) {
        let olho = document.getElementById("img-olho")
        let saldo = document.getElementById("saldo")
        if ( btn.classList.contains("olho-aberto") ) {
            btn.classList.remove("olho-aberto")
            btn.classList.add("olho-fechado")
            olho.src = "../../static/icons/olho-fechado.png"
            saldo.innerHTML = " * * * *"
        } else {
            btn.classList.remove("olho-fechado")
            btn.classList.add("olho-aberto")
            olho.src = "../../static/icons/olho.png"
            saldo.innerHTML = formatCurrency(this.saldo)
        }
    }

}

const global = new Global()

function formatCurrency(value) {
    const cleanedValue = value.replace(/\D/g, '');

    const number = parseFloat(cleanedValue) / 100; 

    const formatter = new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL',
    });

    return formatter.format(number);
}