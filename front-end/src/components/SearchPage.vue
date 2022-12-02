<template>
    <div class="header display-4 fw-normal">
        <h1 class="display-3">BUSQUEMOS A TU ROOMMIE IDEAL</h1>
    </div>
    <div class="inputs body">
        <div class="form-floating" >
            <select class="form-select " id="floatingSelect" aria-label="Floating label select example" >
                <option selected disabled>Escoge el distrito donde quisieras vivir</option> <option value="">ANCON</option>
                <option value="" >ATE</option> <option value="">BARRANCO</option> <option value="">BREÑA</option>
                <option value="">CARABAYLLO</option> <option value="">CHACLACAYO</option> <option value="">CHORRILLOS</option>
                <option value="">CIENEGUILLA</option> <option value="">COMAS</option> <option value="">EL AGUSTINO</option>
                <option value="">INDEPENDENCIA</option> <option value="">JESUS MARIA</option><option value="">LA MOLINA</option>
                <option value="">LA VICTORIA</option><option value="">LIMA</option><option value="">LINCE</option>
                <option value="">LOS OLIVOS</option><option value="">LURIGANCHO</option><option value="">LURIN</option>
                <option value="">MAGDALENA DEL MAR</option><option value="">MIRAFLORES</option><option value="">PACHACAMAC</option>
                <option value="">PUCUSANA</option><option value="">PUEBLO LIBRE</option><option value="">PUENTE PIEDRA</option>
                <option value="">PUNTA HERMOSA</option><option value="">PUNTA NEGRA</option><option value="">RIMAC</option>
                <option value="">SAN BARTOLO</option><option value="">SAN BORJA</option><option value="">SAN ISIDRO</option>
                <option value="">SAN JUAN DE LURIGANCHO</option><option value="">SAN JUAN DE MIRAFLORES</option>
                <option value="">SAN LUIS</option><option value="">SAN MARTIN DE PORRES</option><option value="">SAN MIGUEL</option>
                <option value="">SANTA ANITA</option><option value="">SANTA MARIA DEL MAR</option>
                <option value="">SANTA ROSA</option><option value="">SANTIAGO DE SURCO</option>
                <option value="">SURQUILLO</option><option value="">VILLA EL SALVADOR</option>
                <option value="">VILLA MARIA DEL TRIUNFO</option>
            </select>
            <label for="floatingSelect">Distrito</label>
        </div>
        <div class="form-floating monto">
            <input type="text" class="form-control" id="floatingPassword" placeholder="¿Cuánto estarías dispuesto a pagar por una habitación?" v-model="query.monto">
            <label for="floatingPassword">Monto Maximo en Soles</label>
        </div>
        <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
            <button type="submit" class="btn btn-primary btn-lg" @click="searchUsers">Buscar</button>
        </div>
    </div>

    
</template>
    
<script>
import axios from 'axios';
/*get the value of inputs and return it*/
export default{
    data() {
        return {
            query: {
                distrito: "",
                monto: ""
            }
        }
    },
    methods: {
        searchUsers() {
            var temp = this.query.distrito = document.getElementById("floatingSelect");
            this.query.distrito = temp.options[temp.selectedIndex].text;
            console.log(this.query.distrito);
            let json ={
                "distrito": this.query.distrito,
                "monto": this.query.monto
            }
            let config = {
                headers: {
                    "Content-Type": "application/json"
                }
            }
            axios.post('http://127.0.0.1:5000/search', json, config)
                .then(data => {
                    axios.post('http://127.0.0.1:5000/search', this.query).then(data =>{
                        localStorage.removeItem(temp);
                        localStorage.removeItem("usuarios")
                        localStorage.setItem("set_distrito",this.query.distrito)     
                        this.$router.push("/profiles");
                })
                });

        }
    }
}
</script>

<style scoped>
.inputs{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 10%;
    margin-left: 10%;
}
.form-floating{
    margin: 10px;
    width: 30%;
    text-align: center;
    /*align text in the middle*/
}
.display-4 {
    font-size: calc(1.475rem + 2.7vw);
    font-weight: 300;
    line-height: 1.2;
    display: block;
    font-size: 2em;
    font-weight: bold;
    text-align: center!important;
}
.monto{
    margin-top: 0.5%;
    margin-bottom: 1.5%;
}
</style>