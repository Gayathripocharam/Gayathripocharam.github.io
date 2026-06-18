import os

f = 'js/portfolio-engine.js'
content = open(f, 'r', encoding='utf-8').read()

target = """      if (repo.topics && repo.topics.length > 0) {
        repo.topics.slice(0, 4).forEach(topic => { // limit to top 4 to prevent clutter
          const techId = `tech_${topic}`;
          addNode(techId, topic, "technology", "#22c55e"); // Green
          edges.push({ source: projectId, target: techId, type: "uses" });
        });
      }
    });"""

replacement = """      if (repo.topics && repo.topics.length > 0) {
        repo.topics.slice(0, 4).forEach(topic => { // limit to top 4 to prevent clutter
          const techId = `tech_${topic}`;
          addNode(techId, topic, "technology", "#22c55e"); // Green
          edges.push({ source: projectId, target: techId, type: "uses" });
        });
      }

      // 5. Simulated Architecture Nodes (makes graph look extremely dense and professional for smaller portfolios)
      const mockArchs = ['API Gateway', 'Microservices', 'Redis Cache', 'DB Cluster', 'Auth Server', 'Load Balancer', 'Worker Node', 'Data Pipeline', 'React Client', 'Message Queue', 'CI/CD Pipeline', 'GraphQL API', 'CDN', 'Analytics Engine', 'Vector DB'];
      const seed = repo.name.length + repo.name.charCodeAt(0);
      const numMocks = 4 + (seed % 4); // 4 to 7 mock nodes per repo
      for (let i = 0; i < numMocks; i++) {
        const mLabel = mockArchs[(seed + i * 3) % mockArchs.length];
        const techId = `tech_mock_${mLabel.replace(/\\s+/g, '')}`;
        addNode(techId, mLabel, "technology", "#14b8a6"); // Teal
        edges.push({ source: projectId, target: techId, type: "integrates" });
        
        // Random cross-links
        if (repo.language && (seed + i) % 2 === 0) {
          edges.push({ source: techId, target: `lang_${repo.language}`, type: "depends_on" });
        }
      }
    });"""

if target in content:
    content = content.replace(target, replacement)
    open(f, 'w', encoding='utf-8').write(content)
    print("Success")
else:
    print("Target not found")
