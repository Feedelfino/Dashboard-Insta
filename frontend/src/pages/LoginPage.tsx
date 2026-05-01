import {useState} from 'react'

function LoginPage() {

  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')

async function handleLogin() {
  try {
    const resposta = await fetch('http://127.0.0.1:8000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        senha,
      }),
    })

    const dados = await resposta.json()

    console.log('Resposta backend:', dados)

    // Se backend respondeu erro
    if (!resposta.ok || dados.erro) {
      alert(dados.erro || 'Login inválido')
      return
    }
// Salva o token JWT no navegador
// Esse token será usado depois para acessar rotas protegidas, como /metrics
localStorage.setItem('token', dados.access_token)
    
    alert('Login realizado com sucesso!')

    // Redireciona o usuário para a tela principal após login
    window.location.href = '/dashboard'

  } catch (error) {
      console.error(error)
    alert('Erro ao conectar backend')
  }
}

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>Dashboard Insta Analytics</h1>

        <input
          type="email"
          placeholder="Seu e-mail"
          style={styles.input}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Sua senha"
          style={styles.input}
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
        />
        <button style={styles.button} onClick={handleLogin}>
          Entrar
        </button>
      </div>
    </div>
  )
}

const styles = {
  container: {
    height: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    background: '#f4f6f8',
  },

  card: {
    background: '#ffffff',
    padding: '40px',
    borderRadius: '12px',
    width: '350px',
    boxShadow: '0 8px 25px rgba(0,0,0,0.08)',
    display: 'flex',
    flexDirection: 'column' as const,
    gap: '15px',
  },

  title: {
    marginBottom: '10px',
    fontSize: '28px',
  },

  input: {
    padding: '12px',
    borderRadius: '8px',
    border: '1px solid #ccc',
    fontSize: '16px',
  },

  button: {
    padding: '12px',
    border: 'none',
    borderRadius: '8px',
    background: '#2563eb',
    color: '#fff',
    fontSize: '16px',
    cursor: 'pointer',
  },
}

export default LoginPage
