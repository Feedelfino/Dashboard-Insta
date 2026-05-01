import { useEffect, useState } from 'react'
import { Navigate } from 'react-router-dom'

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
        <div>
          <p>Seguidores: {metric.seguidores}</p>
          <p>Alcance: {metric.alcance}</p>
          <p>Impressões: {metric.impressoes}</p>
          <p>Atualizado em: {metric.criado_em}</p>
        </div>
      )}
    </div>
  )
}

export default DashboardPage