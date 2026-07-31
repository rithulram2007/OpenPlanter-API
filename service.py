from agent.builder import build_engine
from agent.runtime import SessionRuntime
from agent.config import AgentConfig
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
import os

print("OPENROUTER_API_KEY =", os.getenv("OPENROUTER_API_KEY"))
print("OPENPLANTER_PROVIDER =", os.getenv("OPENPLANTER_PROVIDER"))

class OpenPlanterService:
    def __init__(self):
        cfg = AgentConfig.from_env(Path.cwd())
        cfg.provider = "openrouter"
        engine = build_engine(cfg)
        self.runtime = SessionRuntime.bootstrap(
            engine=engine,
            config=cfg,
        )

    def solve(self, task: str):
        return self.runtime.solve(task)