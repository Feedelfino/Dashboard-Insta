import { useEffect, useState } from 'react'
import { Navigate } from 'react-router-dom'
import {LineChart,
        Line,
        XAxis,
        YAxis,
        Tooltip,
        CartesianGrid,
        ResponsiveContainer,
      } from 'recharts'

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

  function formatarData(data: string) {
    return new Date(data).toLocaleDateString('pt-BR')
  }

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
    <div style={styles.container}>
    <div style={styles.header}>
      <div>
        <h1 style={styles.title}>Dashboard de Métricas</h1>
        <p style={styles.subtitle}>
          Acompanhe os principais indicadores do perfil em tempo real.
          </p>
      </div>
     </div> 

      {loading && (
        <div style={styles.loadingBox}>
          <p style={styles.loadingText}>
            Carregando métricas...
          </p>
        </div>
      )}

      {!loading && !metric && (
        <p>Nenhuma métrica encontrada.</p>
      )}

      {!loading && metric && (
        <div style={styles.grid}>
          <div style={styles.card}>
            <h3 style={styles.cardTitle}>seguidores</h3>
            <p style={styles.cardValue}>{metric.seguidores}</p>
        </div>

        <div style={styles.card}>
            <h3 style={styles.cardTitle}>Alcance</h3>
            <p style={styles.cardValue}>{metric.alcance}</p>
        </div>

        <div style={styles.card}>
          <h3 style={styles.cardTitle}>Impressões</h3>
          <p style={styles.cardValue}>{metric.impressoes}</p>
        </div>
        </div>
      )}

      {historico.length >0 && (
        <div style={styles.chartBox}>
          <h2>Evolução de Seguidores</h2>

          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={historico}>
              <CartesianGrid stroke="#ccc" />
              <XAxis 
              dataKey="criado_em"
              tickFormatter={formatarData} />
              <YAxis />
              <Tooltip/>
              <Line 
                type="monotone" 
                dataKey="seguidores" 
                stroke="#2563eb"/>
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>  
  )
}


const styles = {
  
  loadingBox: {
    marginTop: '20px',
    padding: '20px',
    background: '#ffffff',
    borderRadius: '12px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
  },

  loadingText: {
    margin:0,
    color: '#666',
  },

  container: {
    padding: '40px',
    maxWidth: '1000px',
    margin: '0 auto',
  },

  header: {
    marginBottom: '30px',
  },

  title: {
    fontSize: '32px',
    marginBotton: '8px',
  },

  subtitle: {
    color: '#666',
    fontSize: '16px',
    margin: 0,
  },

  grid: {
    display: 'flex',
    gap: '20px',
    marginTop: '20px',
  },

  cardTitle: {
    fontSize: '14px',
    color: '#666',
    margin: 0
  },

  cardValue: {
    fontSize: '32px',
    fontWeigth: 'bold' as const,
    margin: 0,
  },

  card: {
    background: '#ffffff',
    padding: '20px',
    borderRadius: '12px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
    minWidth: '150px',
    display: 'flex',
    flexDirection: 'column'as const,
    gap: '10px',
  },

  chartBox: {
    marginTop:'40px',
    background: '#ffffff',
    padding: '24px',
    borderRadius: '12px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.08)',
  },
}

export default DashboardPage