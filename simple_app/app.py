from flask import Flask, render_template, abort
import os
import yaml
import markdown

app = Flask(__name__)

def get_blogs():
    blogs = []
    blog_dir = 'blogs'
    if os.path.exists(blog_dir):
        # Read all markdown files in the blogs directory
        for filename in sorted(os.listdir(blog_dir), reverse=True):
            if filename.endswith(".md"):
                filepath = os.path.join(blog_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract frontmatter (the metadata between --- lines)
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            metadata = yaml.safe_load(parts[1])
                            body = parts[2].strip()
                            blogs.append({
                                'title': metadata.get('title', 'Untitled'),
                                'date': metadata.get('date', 'Unknown Date'),
                                'summary': body[:150] + '...' if len(body) > 150 else body,
                                'slug': filename[:-3]
                            })
    return blogs

@app.route("/")
def home():
    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)

@app.route("/blog/<slug>")
def blog_post(slug):
    filepath = os.path.join('blogs', f"{slug}.md")
    if not os.path.exists(filepath):
        abort(404)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    metadata = {}
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            metadata = yaml.safe_load(parts[1])
            body = parts[2].strip()
            
    html_content = markdown.markdown(body, extensions=['extra', 'codehilite'])
    
    return render_template('post.html', title=metadata.get('title', 'Blog Post'), date=metadata.get('date', ''), content=html_content)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
