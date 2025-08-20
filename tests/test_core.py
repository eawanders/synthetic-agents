from synthetic_agents.agent import Agent

def test_agent_moves():
    a=Agent(id=1,x=0)
    a.step()
    assert a.x in (-1,1)
