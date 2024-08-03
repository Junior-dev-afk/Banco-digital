class Pix {

    constructor () {

        this.chave = false
        this.senha = false
        this.valor = ""

    }

    async enviar () {

        let pagador = await global.getSession()
        let senha = global.getPassword()
        let chave = this.chave
        let valor = this.valor

        let response = await fetch("/enviarPix", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({pagador : pagador, senha : senha, chave : chave, valor : valor})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao enviar pix")
        }

        let data = await response.json()

        if ( data.response != true ) {
            global.notify(data.response)
            return window.location.href = `${window.location.origin}/home`
        }

        global.notify("Pix enviado com sucesso")

        return window.location.href = `${window.location.origin}/home`
    }

    async goForPageValue () {

        let user = await global.getSession()

        let chave = document.querySelector(".chavePix").value

        let response = await fetch("/verifyChavePix", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({chave : chave, user : user})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao verificar chave pix")
        }

        let data = await response.json()


        if ( data.response == true ) {
            let container = document.querySelector(".container-app")
            let conteudo = `
                <input placeholder="Valor" type="text" oninput="updateFormattedValue(this)" class="valor">
                <button onclick="pix.goForConfirmar()" class="button_pix">Transferir</button>
            `
            this.chave = chave
            container.innerHTML = conteudo
            return  clearInputs();
        }

        global.notify(data.response)
    }

    async goForConfirmar () {

        let user = await global.getSession()

        let valor = document.querySelector(".valor").value
        valor = valor.replace(/\D/g, '');

        if ( valor <= 0 ) {
            global.notify("O valor deve ser maior que zero")
        }

        console.log(valor);

        let response = await fetch("/verifyValor", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({valor : valor, user : user})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao verificar valor na conta")
        }

        let data = await response.json()

        if (data.response == true){
            let container = document.querySelector(".container-app")
            let conteudo = `
                <input placeholder="Senha" oninput="verificarSenhaAuto(this)" type="text" class="senha">
            `
            this.valor = valor
            container.innerHTML = conteudo
            return  clearInputs();
        }

        global.notify(data.response)

    }

    async getNameFromChave () {
        let response = await fetch("/getUserFromChave", {
            method : "POST",
            headers : {
                "Content-Type" : "application/json"
            },
            body : JSON.stringify({chave : this.chave})
        })

        if ( !response.ok ) {
            throw new Error("Erro ao verificar nome de usuario por chave pix")
        }

        let data = await response.json()

        return data.response.user
    }

    async goForConfirmarEnvio() {
        let container = document.querySelector(".container-app")
        let conteudo = `
            <div style="padding-left: 100px; display: flex; flex-direction: column; width: 100%; height: 100%; justify-content: start;" class="container-confirmar">
                <label style="margin: 10px; font-size: 25px;" for="">Transferindo</label>
                <label style="margin: 10px; font-size: 30px;" for="">${formatCurrency(this.valor)}</label>
                <label style="margin: 10px; font-size: 14px;" style="margin-top: 30px;" for="">para <strong>${await this.getNameFromChave()}</strong></label>
                <div  style="margin: 10px;">
                    <label for="">cpf</label>
                    <label style="margin-left: 50px;" for="">${this.chave}</label>
                </div>
                <button onclick="pix.enviar()" style="color: white; margin-top: 20px; border: none; outline: 1px solid black; border-radius: 10px; width: 150px; height: 35px; background-color: rgb(1, 150, 1);">Transferir</button>
            </div>
        `
        container.innerHTML = conteudo
    }

}

const pix = new Pix()

function verificarSenhaAuto( input ) {
    console.log(input.value);
    let senha = global.getPassword()
    if ( input.value == senha ) {
        pix.goForConfirmarEnvio()
    }
}


function updateFormattedValue(input) {

    const rawValue = input.value;
    const formattedValue = formatCurrency(rawValue);

    input.value = formattedValue;
}

function clearInputs() {
    const inputs = document.querySelectorAll('input');
    
    inputs.forEach(input => {
        input.value = '';
    });
}

