import os
import re

# Update Services_page.html
services_file = 'Services_page.html'
with open(services_file, 'r', encoding='utf-8') as f:
    services_html = f.read()

# Replace headline
services_html = re.sub(
    r'<p class="mx-auto mt-6 max-w-2xl text-lg text-slate-600">.*?</p>',
    '<p class="mx-auto mt-6 max-w-2xl text-lg text-slate-600">\n            Data Science Student building scalable, data-driven solutions with machine learning, analytics, and modern web technologies.\n          </p>',
    services_html,
    flags=re.DOTALL
)

# Replace the grid cards
new_cards = '''          <!-- 1. Data Analysis & Visualization -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18" /><path d="M18 9l-5 5-3-3-4 4" /></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">Data Analysis & Visualization</h2>
              <p class="text-slate-600 text-sm">Transforming raw data into meaningful insights using statistical analysis and interactive visualizations.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Python</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Pandas</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Matplotlib</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Seaborn</span>
              </div>
            </div>
          </div>

          <!-- 2. Machine Learning Models -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"></path><circle cx="12" cy="10" r="3"></circle><path d="M2 12c2-6 6-8 10-8s8 2 10 8c-2 6-6 8-10 8s-8-2-10-8z"></path></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">Machine Learning Models</h2>
              <p class="text-slate-600 text-sm">Building predictive models using supervised and unsupervised learning techniques for real-world datasets.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Scikit-learn</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Regression</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Classification</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Clustering</span>
              </div>
            </div>
          </div>

          <!-- 3. Data Cleaning & Preprocessing -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">Data Cleaning & Preprocessing</h2>
              <p class="text-slate-600 text-sm">Handling missing data, feature engineering, and preparing datasets for accurate model performance.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Data Wrangling</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Feature Engineering</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">NumPy</span>
              </div>
            </div>
          </div>

          <!-- 4. Data Science Web Applications -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18M7 7v10M17 7v10"></path><rect x="4" y="17" width="16" height="4" rx="1.5"></rect></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">Data Science Web Applications</h2>
              <p class="text-slate-600 text-sm">Developing interactive web apps to deploy machine learning models and visualize results.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Flask</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Streamlit</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">APIs</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Deployment</span>
              </div>
            </div>
          </div>

          <!-- 5. Statistical Analysis -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">Statistical Analysis</h2>
              <p class="text-slate-600 text-sm">Applying statistical techniques to interpret data, identify trends, and support decision-making.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Hypothesis Testing</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Probability</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">EDA</span>
              </div>
            </div>
          </div>

          <!-- 6. AI & Deep Learning -->
          <div class="flex flex-col gap-4 rounded-3xl bg-white/60 backdrop-blur-xl border border-white/50 p-6 shadow-xl shadow-indigo-500/5 ring-1 ring-white/50 hover-float scroll-reveal">
            <div class="text-primary">
              <svg class="w-9 h-9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
            </div>
            <div class="flex flex-col gap-2">
              <h2 class="text-xl font-semibold text-slate-900">AI & Deep Learning</h2>
              <p class="text-slate-600 text-sm">Exploring neural networks and deep learning models for advanced data-driven solutions.</p>
              <div class="mt-3 flex flex-wrap gap-2">
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">TensorFlow</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Keras</span>
                <span class="text-xs px-2 py-1 bg-primary/10 text-primary rounded">Neural Networks</span>
              </div>
            </div>
          </div>'''

services_html = re.sub(
    r'(<div class="scroll-reveal mt-16 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3" data-stagger-list>).*?(?=</section>)',
    r'\1\n' + new_cards + '\n        </div>\n      </div>\n    ',
    services_html,
    flags=re.DOTALL
)

with open(services_file, 'w', encoding='utf-8') as f:
    f.write(services_html)

# Update Portfolio_page.html
portfolio_file = 'Portfolio_page.html'
with open(portfolio_file, 'r', encoding='utf-8') as f:
    portfolio_html = f.read()

# Remove Blockchain and Security buttons
portfolio_html = re.sub(r'<button[^>]*data-filter="Blockchain"[^>]*>Blockchain</button>\s*', '', portfolio_html)
portfolio_html = re.sub(r'<button[^>]*data-filter="Security"[^>]*>Security</button>\s*', '', portfolio_html)

# Add Data Analytics button right after Data Science
portfolio_html = re.sub(
    r'(<button[^>]*data-filter="Data Science"[^>]*>Data Science</button>\s*)',
    r'\1<button class="filter-pill px-4 py-1.5 text-xs font-bold rounded-full border border-slate-200 text-slate-600 hover:border-primary/40 hover:text-primary" data-filter="Data Analytics">Data Analytics</button>\n          ',
    portfolio_html
)

with open(portfolio_file, 'w', encoding='utf-8') as f:
    f.write(portfolio_html)

print("Updates to Services and Portfolio complete!")
