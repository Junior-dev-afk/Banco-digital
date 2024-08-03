class Anim {
    constructor(){
        this.page = "login"
    }

    register_to_login() {
        if (this.page == "register") {
            this.page = "login"
            let t = document.querySelector(".tampador")
            t.classList.add("anim_login_to_register")
            setTimeout(() => {
                t.classList.remove("tampador_left")
                t.classList.remove("anim_login_to_register")
                t.classList.add("tampador_right")
            }, 1450)
        }
    }

    login_to_register () {
        if ( this.page == 'login' ) {
            this.page = "register"
            let t = document.querySelector(".tampador")
            t.classList.add("anim_register_to_login")
            setTimeout(()=>{
                t.classList.remove("tampador_right")
                t.classList.remove("anim_register_to_login")
                t.classList.add("tampador_left")
            }, 1450)
        }
    }
}

const animation = new Anim()