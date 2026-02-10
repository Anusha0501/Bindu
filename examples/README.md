# 🌻 Bindu Examples Gallery

Welcome to the **Bindu Examples Gallery** - your gateway to mastering AI agent development! This curated collection showcases the full spectrum of what's possible with Bindu, from simple echo bots to sophisticated multi-agent systems with payment integration.

## 🎯 What You'll Discover

- **🚀 Quick Start**: Get running in minutes with zero-config agents
- **🧠 Intelligent Agents**: Research, summarize, and analyze with advanced AI
- **💰 Monetization**: Build paid agents with X402 payment protocol
- **🤝 Multi-Agent Systems**: Coordinate teams of specialized agents
- **🔧 Real Integrations**: Connect with Notion, weather APIs, and more
- **🏥 Specialized Applications**: Healthcare, finance, and therapy agents

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.12+** - Modern Python with latest features
- **uv package manager** - Fast Python package installer
- **OpenRouter API key** - Access to advanced AI models

### Installation

```bash
# Clone the repository
git clone https://github.com/getbindu/bindu.git
cd bindu

# Install dependencies
uv sync --dev

# Set up your API key
export OPENROUTER_API_KEY="your-key-here"
```

### Run Your First Agent

```bash
# Try the simplest agent - perfect for testing
uv run examples/beginner/echo_simple_agent.py

# Or jump to zero-config for instant functionality
uv run examples/beginner/beginner_zero_config_agent.py
```

Each agent starts on its own port (usually 3773-3780) and provides an interactive chat interface at `http://localhost:[port]/docs`

## 📚 Complete Agent Catalog

### 🌱 Beginner Agents
*Perfect for learning Bindu fundamentals and getting started quickly*

| Agent | File | Description | Features | 🚀 Quick Start |
|-------|------|-------------|----------|----------------|
| **Echo Bot** | `beginner/echo_simple_agent.py` | Minimal agent that echoes input | Ultra-minimal, no dependencies | `uv run examples/beginner/echo_simple_agent.py` |
| **Zero Config** | `beginner/beginner_zero_config_agent.py` | Instant agent with web search | Zero setup, friendly responses | `uv run examples/beginner/beginner_zero_config_agent.py` |
| **Joke Master** | `beginner/agno_simple_example.py` | Entertainment agent | Humor generation, topic-specific jokes | `uv run examples/beginner/agno_simple_example.py` |
| **Research Assistant** | `beginner/agno_example.py` | Web-powered research | DuckDuckGo integration, comprehensive analysis | `uv run examples/beginner/agno_example.py` |
| **FAQ Expert** | `beginner/faq_agent.py` | Bindu documentation searcher | Web search, markdown responses, citations | `uv run examples/beginner/faq_agent.py` |
| **Notion Integrator** | `beginner/agno_notion_agent.py` | Content management for Notion | Page creation, database search | `uv run examples/beginner/agno_notion_agent.py` |

### 🎯 Specialized Agents
*Domain-specific agents for particular use cases and industries*

| Agent | Folder | Description | Features | 🚀 Quick Start |
|-------|--------|-------------|----------|----------------|
| **Text Summarizer** | `summarizer/` | Professional text condensation | Intelligent summarization, key point preservation | `uv run examples/summarizer/summarizer_agent.py` |
| **Weather Research** | `weather-research/` | Real-time weather intelligence | Global coverage, search-powered data | `uv run examples/weather-research/weather_research_agent.py` |
| **Premium Advisor** | `premium-advisor/` | Market insights with payment gating | **X402 Payments**, 0.01 USDC per query | `uv run examples/premium-advisor/premium_advisor.py` |

### 🚀 Advanced Multi-Agent Systems
*Complex orchestration examples showcasing Bindu's agent coordination capabilities*

| System | Folder | Description | Architecture | 🚀 Quick Start |
|--------|--------|-------------|-------------|----------------|
| **Agent Swarm** | `agent_swarm/` | Collaborative intelligence system | 5 specialized agents (Planner → Researcher → Summarizer → Critic → Reflection) | `uv run examples/agent_swarm/bindu_super_agent.py` |
| **CBT Therapy** | `cerina_bindu/cbt/` | Therapeutic protocol generation | LangGraph workflow (Drafter → Safety Guardian → Clinical Critic) | `uv run examples/cerina_bindu/cbt/supervisor_cbt.py` |

### 🔧 Skills & Components
*Reusable agent capabilities and building blocks*

| Component | Location | Purpose | Used In |
|-----------|----------|---------|----------|
| **CBT Skills** | `skills/cbt-*` | Therapy protocol components | CBT Therapy System |
| **ZK Policy** | `skills/zk-policy/` | Zero-knowledge verification | Security & Compliance |

---

## 💰 Spotlight: Premium Advisor Agent

> **Experience the future of AI monetization with X402 payments!**

The `premium-advisor/` example demonstrates Bindu's revolutionary **X402 payment protocol** - enabling you to build paid AI services that require payment before execution.

### How It Works
1. **User sends message** → Agent receives request
2. **Payment required** → 402 response with payment details (0.01 USDC)
3. **User pays** → Cryptocurrency transaction on Base Sepolia
4. **Payment verified** → Agent executes and delivers premium insights
5. **Revenue earned** 💰 → Funds go to your specified address

### Try It Now
```bash
# Start the premium advisor
uv run examples/premium-advisor/premium_advisor.py

# Visit http://localhost:3773/docs
# Send: "What are the best investment opportunities right now?"
# Complete the 0.01 USDC payment
# Receive professional market insights!
```

**This is how you monetize AI agents natively!** 🚀

## 🔗 Agent Quick Links

### 🌱 Beginner Agents
- [📝 Echo Bot](beginner/echo_simple_agent.py) - *Minimal testing agent*
- [⚡ Zero Config](beginner/beginner_zero_config_agent.py) - *Instant functionality*
- [😄 Joke Master](beginner/agno_simple_example.py) - *Entertainment focused*
- [🔍 Research Assistant](beginner/agno_example.py) - *Web-powered research*
- [❓ FAQ Expert](beginner/faq_agent.py) - *Documentation searcher*
- [📋 Notion Integrator](beginner/agno_notion_agent.py) - *Content management*

### 🎯 Specialized Agents
- [📄 Text Summarizer](summarizer/) - *Professional content condensation*
- [🌤️ Weather Research](weather-research/) - *Real-time weather intelligence*
- [💎 Premium Advisor](premium-advisor/) - *Paid market insights*

### 🚀 Advanced Systems
- [🤖 Agent Swarm](agent_swarm/) - *Multi-agent collaboration*
- [🏥 CBT Therapy](cerina_bindu/cbt/) - *Therapeutic protocols*

### 🔧 Components
- [🧩 Skills Library](skills/) - *Reusable agent capabilities*

---

## ⚙️ Environment Configuration

### Required Environment Variables

Most examples need these core variables:

```bash
# OpenRouter API - Required for all agents
OPENROUTER_API_KEY=sk-or-v1-your-api-key-here

# Bindu Authentication (default)
HYDRA__ADMIN_URL=https://hydra-admin.getbindu.com
HYDRA__PUBLIC_URL=https://hydra.getbindu.com
```

### Optional Infrastructure

```bash
# PostgreSQL for persistent storage
DATABASE_URL=postgresql+asyncpg://user:pass@host/db

# Redis for advanced scheduling
REDIS_URL=rediss://default:pass@host:6379
```

### Quick Setup Script

```bash
# Create .env file for any example
cp examples/[example-folder]/.env.example examples/[example-folder]/.env
# Edit the file and add your OPENROUTER_API_KEY
```

## Spotlight: Premium Advisor Agent

The `premium-advisor/` example demonstrates Bindu's unique **X402** payment protocol. This agent is configured to reject any interaction unless a micropayment is made.

**To run it:**
```bash
uv run examples/premium-advisor/premium_advisor.py
```

**What happens:**
1. **Request**: You send a message to the agent.
2. **402 Payment Required**: The agent intercepts the request and demands payment (0.01 USDC).
3. **Invoice**: The response contains the blockchain details needed to pay.
4. **Service**: Once paid (proved via signature), the agent releases the advice.

This powerful feature allows you to monetize your agents natively!

## 🧪 Testing Your Agents

### Interactive Testing (Recommended)

All agents provide a beautiful web interface:
```bash
# Start any agent, then visit:
http://localhost:[port]/docs
```

### API Testing

#### Basic Request
```bash
curl -X POST http://localhost:3773/ \
     -H "Content-Type: application/json" \
     -d '{
           "jsonrpc": "2.0",
           "method": "message/send",
           "params": {"message": {"role": "user", "content": "Hello!"}},
           "id": 1
         }'
```

#### Authenticated Request
```bash
# Get JWT token from Hydra
curl 'https://hydra.getbindu.com/oauth2/token' \
  --user 'YOUR_DID:YOUR_CLIENT_SECRET' \
  -d 'grant_type=client_credentials' \
  -d 'scope=openid agent:read agent:write'
```

#### Public Endpoints
```bash
# Health check
curl http://localhost:3773/health

# Agent skills
curl http://localhost:3773/agent/skills

# DID resolution
curl -X POST http://localhost:3773/did/resolve \
  -H "Content-Type: application/json" \
  -d '{"did": "YOUR_AGENT_DID"}'
```

## 🎯 Learning Path: From Zero to Hero

### 🌱 Phase 1: Get Started (5 minutes)
1. **Echo Bot** → Verify your setup works
2. **Zero Config** → Experience instant AI functionality

### 🧠 Phase 2: Add Intelligence (15 minutes)
3. **Research Assistant** → Web-powered knowledge
4. **Joke Master** → Creative AI interactions
5. **FAQ Expert** → Documentation mastery

### 🎯 Phase 3: Real Applications (30 minutes)
6. **Text Summarizer** → Content processing
7. **Weather Research** → Real-time data integration
8. **Notion Integrator** → External service connections

### 💰 Phase 4: Monetization (45 minutes)
9. **Premium Advisor** → Experience X402 payments
10. **Payment Integration** → Learn to monetize your agents

### 🚀 Phase 5: Advanced Systems (60+ minutes)
11. **Agent Swarm** → Multi-agent orchestration
12. **CBT Therapy** → Complex workflow integration
13. **Custom Development** → Build your own solutions

### 🔧 Phase 6: Master Level
14. **Skills Development** → Create reusable components
15. **Architecture Design** → Plan complex systems
16. **Production Deployment** → Scale to real users

---

## 🛠️ Development Resources

### 📁 Project Structure
```
examples/
├── 🌱 beginner/                 # Learning agents (6 files)
├── 🎯 specialized/              # Domain-specific agents
│   ├── summarizer/             # Text processing
│   ├── weather-research/        # Real-time data
│   └── premium-advisor/        # Paid services
├── 🚀 advanced/               # Complex systems
│   ├── agent_swarm/           # Multi-agent coordination
│   └── cerina_bindu/          # Therapy workflows
├── 🔧 skills/                 # Reusable components
└── 📚 README.md              # This guide
```

### 🏗️ Architecture Patterns

#### **Simple Agent Pattern**
```python
# Basic structure for most agents
from agno.agent import Agent
from agno.models.openrouter import OpenRouter

agent = Agent(
    instructions="Your agent instructions...",
    model=OpenRouter(id="openai/gpt-oss-120b"),
    tools=[your_tools]
)
```

#### **Payment-Gated Pattern**
```python
# Add X402 payment integration
config = {
    "execution_cost": {
        "amount": "0.01",
        "token": "USDC",
        "network": "base-sepolia"
    }
}
```

#### **Multi-Agent Pattern**
```python
# Coordinate multiple specialized agents
orchestrator = Orchestrator(
    agents=[planner, researcher, summarizer, critic],
    workflow="sequential"
)
```

## 🤝 Community & Support

### 🆘 Getting Help
- **📚 [Documentation](https://docs.getbindu.com)** - Comprehensive guides
- **💬 [Discord Community](https://discord.getbindu.com)** - Chat with developers
- **🐛 [GitHub Issues](https://github.com/getbindu/bindu/issues)** - Report bugs
- **📖 [Examples](https://github.com/getbindu/bindu/tree/main/examples)** - More code samples

### 🎯 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create your agent** in a new folder
3. **Add documentation** with README.md
4. **Submit a pull request**

#### Contribution Guidelines
- ✅ Follow Python PEP 8 standards
- ✅ Include comprehensive README
- ✅ Add proper error handling
- ✅ Test your agent thoroughly
- ✅ Use environment variables for secrets

### 🏆 Showcase Your Agents

Built something amazing? We'd love to feature it!
- **🌟 Star the repository**
- **📝 Share your use case** in our Discord
- **🔗 Submit your example** for inclusion

---

## 🎉 What's Next?

### 🚀 Upcoming Features
- **🎙️ Voice Agents** - Speech-to-speech interactions
- **📁 File Processing** - Document analysis capabilities
- **🔄 Streaming Responses** - Real-time agent outputs
- **🌐 Multi-language Support** - International agents
- **📊 Analytics Dashboard** - Agent performance metrics

### 🎓 Advanced Learning
- **📖 [Bindu Documentation](https://docs.getbindu.com)** - Deep dive into features
- **🎥 [Video Tutorials](https://youtube.com/@getbindu)** - Visual learning
- **🏛️ [Architecture Guide](https://docs.getbindu.com/architecture)** - System design
- **💰 [Monetization Guide](https://docs.getbindu.com/monetization)** - X402 payments

---

## 📄 License

This project is part of the Bindu framework and follows the same [license terms](../LICENSE).

---

**🌻 Built with love by the Bindu Team**

*Identity + Communication + Payments for AI Agents*

---

**Ready to build the future of AI?** 🚀

[Get Started with Echo Bot](beginner/echo_simple_agent.py) • [Explore All Agents](#-agent-quick-links) • [Join Our Community](https://discord.getbindu.com)
