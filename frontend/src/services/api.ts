// Centraliza a URL base da API do backend
const API_URL = 'http://127.0.0.1:8000'

//Busca token salvo no navegador
function getToken() {
    return localStorage.getItem('token')
}

//Headers padrão da aplicação
function getHeaders() {
    return {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${getToken()}`,
    }
}

 //Faz login no usário e retorna os dados da API
 async function login(email: string,senha: string){
    const resposta = await fetch(`${API_URL}/auth/login`, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email,
            senha,
        }),
    })

    const dados = await resposta.json()

    return {
        resposta,
        dados,
    }
 }

    async function buscarMetricas(){

        //Faz requisição GET para o endpoint de métricas
        const resposta = await fetch (`${API_URL}/metrics`, {

            //Usa headers centralizao da aplicação
            headers: getHeaders(),
        })

        //Converte resposta da API para JSON
        const dados = await resposta.json()

        return dados
    }

    async function buscarHistoricoMetricas(){
        const resposta =await fetch(`${API_URL}/metrics/historico`, {
            headers: getHeaders(),
        })
        const dados = await resposta.json()
        return dados
    }

 export {
    API_URL,
    getHeaders,
    login,
    buscarMetricas,
    buscarHistoricoMetricas,
    }