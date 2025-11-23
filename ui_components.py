import streamlit as st

def render_voice_receptionist_ui(token, avatar_url=None):
    """
    Renders the HTML/JS block with professional UI updates.
    """
    
    # Hardcoded realistic avatar (Bella)
    avatar_src = "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop"

    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background-color: #000; overflow: hidden; height: 100vh; width: 100vw; }}
            
            /* FIXED BACKGROUND */
            .app-background {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                z-index: -1;
            }}

            /* Glassmorphism */
            .glass-panel {{
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}

            .scrollbar-hide::-webkit-scrollbar {{ display: none; }}
            
            /* Animations */
            @keyframes pulse-soft {{
                0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }}
                50% {{ transform: scale(1.05); box-shadow: 0 0 0 20px rgba(99, 102, 241, 0); }}
                100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }}
            }}
            .mic-active {{ animation: pulse-soft 2s infinite; }}

            /* Avatar Glow */
            .avatar-glow {{
                box-shadow: 0 0 20px #6366f1, inset 0 0 20px #6366f1;
                border-color: #818cf8;
                transform: scale(1.02);
            }}
            .avatar-transition {{ transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }}
            
            /* Chat Bubbles */
            .chat-user {{ 
                background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); 
                color: white; 
                border-radius: 20px 20px 4px 20px;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
            }}
            .chat-ai {{ 
                background: rgba(255, 255, 255, 0.1); 
                color: #f8fafc; 
                border-radius: 20px 20px 20px 4px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            
            @keyframes slideIn {{
                from {{ opacity: 0; transform: translateY(10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            .msg-animate {{ animation: slideIn 0.3s ease-out forwards; }}
        </style>
    </head>
    <body class="h-screen flex flex-col text-white">

        <div class="app-background"></div>

        <!-- HEADER - LARGER FONT & ICON -->
        <header class="absolute top-0 left-0 w-full p-6 z-20 flex justify-center items-center">
            <div class="glass-panel px-8 py-4 rounded-full flex items-center gap-5 shadow-2xl">
                <div class="w-3 h-3 rounded-full bg-red-500 shadow-[0_0_10px_rgba(239,68,68,0.6)]" id="connection-dot"></div>
                <div class="flex items-center gap-3">
                    <i class="fa-solid fa-wave-square text-indigo-400 text-2xl"></i>
                    <h1 class="text-2xl font-bold tracking-widest text-white drop-shadow-md">LIVE VOICE ASSISTANT</h1>
                </div>
            </div>
        </header>

        <!-- MAIN CONTENT -->
        <main class="flex-grow flex flex-col items-center justify-center p-4 relative w-full h-full">
            
            <!-- ACTIVE CALL UI -->
            <div id="active-call-ui" class="hidden flex-col w-full max-w-3xl h-full pt-28 pb-24">
                
                <!-- Avatars Section -->
                <div class="flex justify-between items-center px-12 mb-8 flex-none">
                    
                    <!-- AI Avatar (Bella) -->
                    <div class="flex flex-col items-center gap-3">
                        <div id="ai-avatar" class="w-32 h-32 rounded-full border-4 border-white/10 flex items-center justify-center avatar-transition overflow-hidden shadow-2xl relative bg-black">
                            <img src="{avatar_src}" alt="Bella" class="w-full h-full object-cover" />
                        </div>
                        <span class="text-white/60 text-xs font-bold tracking-[0.2em] mt-2">BELLA</span>
                    </div>

                    <!-- Visualizer -->
                    <div id="visualizer" class="flex items-center gap-2 h-16 mx-4">
                        <!-- Bars injected by JS -->
                    </div>

                    <!-- User Avatar - COLORFUL ICON -->
                    <div class="flex flex-col items-center gap-3">
                        <div id="user-avatar" class="w-32 h-32 rounded-full bg-gradient-to-br from-pink-500 via-purple-500 to-indigo-500 border-4 border-white/20 flex items-center justify-center avatar-transition shadow-2xl">
                            <i class="fa-solid fa-user text-white text-5xl drop-shadow-lg"></i>
                        </div>
                        <span class="text-white/60 text-xs font-bold tracking-[0.2em] mt-2">YOU</span>
                    </div>
                </div>

                <!-- Chat Area -->
                <div id="chat-container" class="flex-grow glass-panel rounded-3xl p-8 overflow-y-auto scrollbar-hide flex flex-col gap-4 relative mx-4 border-white/5">
                     <div id="placeholder-text" class="absolute inset-0 flex items-center justify-center text-white/20 text-base font-medium pointer-events-none tracking-wide">
                        Connecting to Bella...
                     </div>
                     <div id="chat-log" class="flex flex-col gap-4 pb-4"></div>
                </div>
            </div>

            <!-- START SCREEN UI -->
            <div id="start-screen" class="flex flex-col items-center justify-center z-10 animate-fade-in absolute inset-0">
                
                <!-- Profile Image on Start Screen -->
                <div class="w-40 h-40 rounded-full border-4 border-white/10 overflow-hidden mb-10 shadow-2xl ring-4 ring-white/5">
                     <img src="{avatar_src}" class="w-full h-full object-cover" />
                </div>

                <button id="start-btn" class="w-24 h-24 rounded-full bg-white text-indigo-600 flex items-center justify-center shadow-[0_0_50px_rgba(255,255,255,0.4)] transition-all duration-300 transform hover:scale-110 hover:shadow-[0_0_80px_rgba(255,255,255,0.6)]">
                    <i class="fa-solid fa-phone text-4xl"></i>
                </button>
                <h2 class="text-white text-3xl font-light mt-8 tracking-wide">Tap to Call</h2>
            </div>
            
            <!-- End Call Button (Fixed Bottom) -->
            <div id="controls-footer" class="hidden fixed bottom-10 left-0 w-full flex justify-center z-30">
                 <button onclick="endCall()" class="bg-red-500/90 hover:bg-red-600 text-white px-10 py-4 rounded-full font-bold flex items-center gap-3 transition-all shadow-lg backdrop-blur-md transform hover:scale-105 border border-red-400/50">
                    <i class="fa-solid fa-phone-slash text-lg"></i>
                    <span class="text-lg">End Call</span>
                </button>
            </div>

        </main>

        <!-- SUMMARY MODAL -->
        <div id="summary-modal" class="fixed inset-0 bg-black/90 backdrop-blur-xl hidden items-center justify-center p-6 z-50">
            <div class="bg-slate-900 border border-white/10 rounded-3xl shadow-2xl w-full max-w-md overflow-hidden transform transition-all scale-100">
                <div class="p-6 bg-slate-800/50 flex justify-between items-center border-b border-white/5">
                    <h2 class="text-lg font-semibold text-white flex items-center gap-2">
                        <i class="fa-regular fa-file-lines text-indigo-400"></i> Summary
                    </h2>
                    <button onclick="closeModal()" class="text-white/40 hover:text-white transition-colors"><i class="fa-solid fa-xmark text-xl"></i></button>
                </div>
                <div class="p-6">
                    <div id="summary-content" class="text-slate-300 leading-relaxed text-sm max-h-[40vh] overflow-y-auto font-light">
                        Generating summary...
                    </div>
                </div>
                <div class="p-4 bg-slate-800/30 flex justify-center">
                    <button onclick="closeModal()" class="w-full bg-white text-slate-900 px-6 py-3 rounded-xl text-sm font-bold hover:bg-slate-200 transition-colors">
                        Done
                    </button>
                </div>
            </div>
        </div>

        <script>
            const EPHEMERAL_KEY = "{token}";
            let pc = null;
            let localStream = null;
            let isActive = false;
            let dc = null;
            
            // Audio Context
            let audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            let localAnalyzer = null;
            let remoteAnalyzer = null;
            let dataArrayLocal, dataArrayRemote;

            // Visualizer Setup
            const visualizerContainer = document.getElementById('visualizer');
            for(let i=0; i<6; i++) {{
                const bar = document.createElement('div');
                bar.className = 'w-2 bg-indigo-400 rounded-full transition-all duration-75';
                bar.style.height = '4px';
                bar.id = 'bar-'+i;
                visualizerContainer.appendChild(bar);
            }}

            function updateVisuals(userVol, aiVol) {{
                const combinedVol = Math.max(userVol, aiVol);
                for(let i=0; i<6; i++) {{
                    const h = Math.max(6, Math.min(60, combinedVol * 300 * (Math.random() * 0.5 + 0.8)));
                    document.getElementById('bar-'+i).style.height = h + 'px';
                }}

                const aiAvatar = document.getElementById('ai-avatar');
                const userAvatar = document.getElementById('user-avatar');
                const threshold = 0.01; 

                if (aiVol > threshold) {{
                    aiAvatar.classList.add('avatar-glow');
                    aiAvatar.style.borderColor = '#6366f1';
                }} else {{
                    aiAvatar.classList.remove('avatar-glow');
                    aiAvatar.style.borderColor = 'rgba(255,255,255,0.1)';
                }}

                if (userVol > threshold) {{
                    userAvatar.classList.add('avatar-glow');
                    userAvatar.style.borderColor = '#6366f1';
                }} else {{
                    userAvatar.classList.remove('avatar-glow');
                    userAvatar.style.borderColor = 'rgba(255,255,255,0.1)';
                }}
            }}

            async function startCall() {{
                if (audioCtx.state === 'suspended') await audioCtx.resume();
                const startBtn = document.getElementById('start-btn');
                startBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin text-4xl"></i>';
                
                try {{
                    pc = new RTCPeerConnection();

                    // Remote Audio
                    const audioEl = document.createElement("audio");
                    audioEl.autoplay = true;
                    pc.ontrack = e => {{
                        audioEl.srcObject = e.streams[0];
                        const src = audioCtx.createMediaStreamSource(e.streams[0]);
                        remoteAnalyzer = audioCtx.createAnalyser();
                        remoteAnalyzer.fftSize = 64;
                        src.connect(remoteAnalyzer);
                        remoteAnalyzer.connect(audioCtx.destination);
                        dataArrayRemote = new Uint8Array(remoteAnalyzer.frequencyBinCount);
                    }};

                    // Local Audio
                    localStream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
                    pc.addTrack(localStream.getTracks()[0]);
                    
                    const src = audioCtx.createMediaStreamSource(localStream);
                    localAnalyzer = audioCtx.createAnalyser();
                    localAnalyzer.fftSize = 64;
                    src.connect(localAnalyzer);
                    dataArrayLocal = new Uint8Array(localAnalyzer.frequencyBinCount);

                    // Start Animation
                    isActive = true;
                    requestAnimationFrame(animateLoop);

                    // Data Channel
                    dc = pc.createDataChannel("oai-events");
                    dc.addEventListener("message", (e) => {{
                        const event = JSON.parse(e.data);
                        if (event.type === 'response.audio_transcript.delta') {{
                            appendToLog('assistant', event.delta);
                        }}
                        if (event.type === 'conversation.item.input_audio_transcription.completed') {{
                            appendToLog('user', event.transcript);
                        }}
                    }});
                    
                    // --- AUTO-GREETING LOGIC ---
                    dc.onopen = () => {{
                        const responseCreate = {{
                            type: "response.create",
                            response: {{
                                modalites: ["text", "audio"],
                                instructions: "Say hello to the user enthusiastically."
                            }}
                        }};
                        dc.send(JSON.stringify(responseCreate));
                    }};

                    // Connect
                    const offer = await pc.createOffer();
                    await pc.setLocalDescription(offer);

                    const baseUrl = "https://api.openai.com/v1/realtime";
                    const model = "gpt-4o-realtime-preview-2024-10-01";
                    const sdpResponse = await fetch(`${{baseUrl}}?model=${{model}}`, {{
                        method: "POST",
                        body: offer.sdp,
                        headers: {{
                            Authorization: `Bearer ${{EPHEMERAL_KEY}}`,
                            "Content-Type": "application/sdp"
                        }},
                    }});

                    const answer = {{ type: "answer", sdp: await sdpResponse.text() }};
                    await pc.setRemoteDescription(answer);
                    
                    toggleScreens(true);
                    updateStatus('connected');

                }} catch (err) {{
                    console.error(err);
                    alert("Failed to connect. API Key valid?");
                    startBtn.innerHTML = '<i class="fa-solid fa-phone text-4xl"></i>';
                }}
            }}

            function animateLoop() {{
                if(!isActive) return;
                let userVol = 0;
                let aiVol = 0;
                if (localAnalyzer) {{
                    localAnalyzer.getByteFrequencyData(dataArrayLocal);
                    let sum = 0;
                    dataArrayLocal.forEach(val => sum += val);
                    userVol = sum / dataArrayLocal.length / 255;
                }}
                if (remoteAnalyzer) {{
                    remoteAnalyzer.getByteFrequencyData(dataArrayRemote);
                    let sum = 0;
                    dataArrayRemote.forEach(val => sum += val);
                    aiVol = sum / dataArrayRemote.length / 255;
                }}
                updateVisuals(userVol, aiVol);
                requestAnimationFrame(animateLoop);
            }}

            function endCall() {{
                if (pc) pc.close();
                if (localStream) localStream.getTracks().forEach(track => track.stop());
                isActive = false;
                showSummary();
            }}

            document.getElementById('start-btn').addEventListener('click', startCall);

            function toggleScreens(isCallActive) {{
                const startScreen = document.getElementById('start-screen');
                const callUI = document.getElementById('active-call-ui');
                const footer = document.getElementById('controls-footer');
                
                if (isCallActive) {{
                    startScreen.classList.add('hidden');
                    callUI.classList.remove('hidden');
                    callUI.classList.add('flex');
                    footer.classList.remove('hidden');
                    footer.classList.add('flex');
                }} else {{
                    startScreen.classList.remove('hidden');
                    callUI.classList.add('hidden');
                    callUI.classList.remove('flex');
                    footer.classList.add('hidden');
                    footer.classList.remove('flex');
                    document.getElementById('start-btn').innerHTML = '<i class="fa-solid fa-phone text-4xl"></i>';
                }}
            }}

            function updateStatus(status) {{
                const dot = document.getElementById('connection-dot');
                if(status === 'connected') {{
                    dot.className = "w-3 h-3 rounded-full bg-green-400 animate-pulse shadow-[0_0_10px_rgba(74,222,128,0.6)]";
                }} else {{
                    dot.className = "w-3 h-3 rounded-full bg-red-500 shadow-[0_0_10px_rgba(239,68,68,0.6)]";
                }}
            }}
            
            let currentRole = null;
            let currentMsgDiv = null;

            function appendToLog(role, text) {{
                const log = document.getElementById('chat-log');
                document.getElementById('placeholder-text').classList.add('hidden');
                
                if (role !== currentRole || !currentMsgDiv) {{
                    currentRole = role;
                    const container = document.createElement('div');
                    container.className = `flex w-full ${{role === 'user' ? 'justify-end' : 'justify-start'}} msg-animate`;
                    
                    currentMsgDiv = document.createElement('div');
                    currentMsgDiv.className = `max-w-[85%] px-5 py-3 text-sm font-medium ${{
                        role === 'user' ? 'chat-user' : 'chat-ai'
                    }}`;
                    
                    container.appendChild(currentMsgDiv);
                    log.appendChild(container);
                }}
                currentMsgDiv.innerText += text;
                const scrollContainer = document.getElementById('chat-container');
                scrollContainer.scrollTop = scrollContainer.scrollHeight;
            }}

            function showSummary() {{
                const modal = document.getElementById('summary-modal');
                const content = document.getElementById('summary-content');
                const log = document.getElementById('chat-log');
                
                let transcript = log.innerText || "No conversation.";
                content.innerText = "TRANSCRIPT:\\n\\n" + transcript;
                
                modal.classList.remove('hidden');
                modal.classList.add('flex');
            }}

            function closeModal() {{
                const modal = document.getElementById('summary-modal');
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                
                document.getElementById('chat-log').innerHTML = '';
                document.getElementById('placeholder-text').classList.remove('hidden');
                currentRole = null;
                currentMsgDiv = null;
                
                toggleScreens(false);
                updateStatus('offline');
            }}
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=900, scrolling=False)