# [Project Name] – AI Agent System

## 🧠 Overview
This project is a multi-agent AI system built using OpenAI Agent SDK-style architecture. It includes handoff logic between agents and uses tools to simulate real-world logic.

## 🤖 Agents Involved
- Agent 1: [e.g. CareerAgent / DestinationAgent / NarratorAgent]
- Agent 2: [e.g. SkillAgent / BookingAgent / MonsterAgent]
- Agent 3: [e.g. JobAgent / ExploreAgent / ItemAgent]

## 🧰 Tools Used
- Tool 1: [e.g. get_career_roadmap / get_flights / roll_dice]
- Tool 2: [e.g. suggest_hotels / generate_event]

## 🔄 Handoff Flow
1. Agent 1 handles the user’s input.
2. Hands off to Agent 2 for next step.
3. Agent 3 finishes the interaction.

## ▶️ How to Run
```bash
streamlit run main.py
