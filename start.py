from pyngrok import ngrok
import subprocess

# Stop any existing ngrok tunnels
ngrok.kill()

# Start Streamlit
process = subprocess.Popen(['streamlit', 'run', 'app.py', '--server.port', '8501'])

# Create a public URL with ngrok
public_url = ngrok.connect(8501)
print("Your app is live at:", public_url)
