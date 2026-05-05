import { useEffect, useState } from 'react'
import { Navigate } from 'react-router-dom'
import {LineChart,Line,XAxis,YAxis,Tooltip,CartesianGrid,} from 'recharts'

// Tipo da métrica recebida do backend
type Metric = {
  seguidores: number
  alcance: number
  impressoes: number
  criado_em: string
}

// Dashboard protegido por token
function DashboardPage() {
  const token = localStorage.getItem('token')

  const [metric, setMetric] = useState<Metric | null>(null)
  const [loading, setLoading] = useState(true)
  const [historico, setHistorico] = useState<Metric[]>([])

  useEffect(() => {
    async function buscarMetricas() {
      try {
        const resposta = await fetch('http://127.0.0.1:8000/metrics', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })

        const dados = await resposta.json()

        console.log('Dados recebidos:', dados)

        if (!resposta.ok) {
          alert('Erro ao buscar métricas')
          return
        }

        setMetric(dados)

     // Busca a lista para por no gráfico   
        const respostaHistorico = await fetch('http://127.0.0.1:8000/metrics/historico', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
     })
     
     
      const dadosHistorico = await respostaHistorico.json()
        
        setHistorico(dadosHistorico)

      } catch (error) {
        console.error(error)
      } finally {
        setLoading(false)
      }
    }

    if (token) {
      buscarMetricas()
    }
  }, [token])

  if (!token) {
    return <Navigate to="/" replace />
  }

  return (
    <div>
      <h1>Dashboard</h1>

      {loading && <p>Carregando métricas...</p>}

      {!loading && !metric && (
        <p>Nenhuma métrica encontrada.</p>
      )}

      {!loading && metric && (
        <div style={styles.grid}>
          <div style={styles.card}>
            <h3>seguidores</h3>
            <p>{metric.seguidores}</p>
        </div>

        <div style={styles.card}>
            <h3>Alcance</h3>
            <p>{metric.alcance}</p>
        </div>

        <div style={styles.card}>
          <h3>Impressões</h3>
          <p>{metric.impressoes}</p>
        </div>
        </div>
      )}

      {historico.length >0 && (
        <div style={styles.chartBox}>
          <h2>Evolução de Seguidores</h2>

          <LineChart width={600} height={300} data={historico}>
            <CartesianGrid stroke='#ccc' />
            <XAxis dataKey="criado_em" />
            <YAxis />
            <Tooltip/>
            <Line type="monotone" dataKey="seguidores" stroke="#2563eb"/>
          </LineChart>
        </div>
      )}
    </div>  
  )
}


const styles = {
  grid: {
    display: 'flex',
    gap: '20px',
    marginTop: '20px',
  },

  card: {
    background: '#ffffff',
    padding: '20px',
    borderRadius: '12px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
    minWidth: '150px',
  },

    chartBox: {
      marginTop: '40px',
  },
}

export default DashboardPage