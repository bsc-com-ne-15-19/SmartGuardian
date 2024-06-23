/**
 * Custom hook for WebSocket communication.
 *
 * @param {Object} options - The options for the WebSocket connection.
 * @param {string} options.url - The URL of the WebSocket server.
 * @returns {Array} - An array containing the WebSocket connection status, received value, and a function to send data.
 */
import { useRef, useState, useEffect } from "react"

export const useWs = ({ url }) => {
    const [isReady, setIsReady] = useState(false)
    const [val, setVal] = useState(null)
  
    const ws = useRef(null)
  
    useEffect(() => {
      const socket = new WebSocket(url)
  
      socket.onopen = () => setIsReady(true)
      socket.onclose = () => setIsReady(false)
      socket.onmessage = (event) => setVal(event.data)
  
      ws.current = socket
  
      return () => {
        socket.close()
      }
    }, [])
  
    // bind is needed to make sure `send` references correct `this`
    return [isReady, val, ws.current?.send.bind(ws.current)]
  }