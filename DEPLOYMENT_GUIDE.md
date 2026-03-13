# How to Deploy Your Python Portfolio with a Custom Domain (HTTPS)

This guide takes you through deploying this exact folder (`simple_app`) to **Render.com** and connecting it to a custom domain with absolute simplicity.

## Step 1: Upload Your Code to GitHub
1. Create an account on [GitHub](https://github.com/).
2. Create a new repository (e.g., `my-portfolio`).
3. Upload the files inside the `simple_app` folder (`app.py`, `requirements.txt`, `templates/`, `static/`) into that repository.

## Step 2: Host on Render.com (Free & Simple)
1. Go to [Render.com](https://render.com/) and sign up with your GitHub account.
2. Click **New +** and select **Web Service**.
3. Select the GitHub repository you just created (`my-portfolio`).
4. Fill in the deployment details:
   - **Name**: `my-portfolio`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (This tells Render to run your Flask app in production mode)
5. Select the **Free** plan and scroll down to click **Create Web Service**.
6. Wait 2-3 minutes. Once it says "Live" in the console, your site is officially on the internet! It will look something like `https://my-portfolio.onrender.com`.

## Step 3: Buy a Domain Name
To have your own name (`https://yourname.com`), you need to buy a domain.
1. Go to a domain registrar like [Namecheap](https://www.namecheap.com/) or [GoDaddy](https://www.godaddy.com/).
2. Search for `yourname.com` and purchase it.

## Step 4: Connect the Custom Domain to Render 
1. Go back to your Render dashboard and click on your "Web Service".
2. On the left sidebar, click **Settings** and scroll down to **Custom Domains**.
3. Click **Add Custom Domain** and type `yourname.com`.
4. Render will provide you with a DNS record (usually a `CNAME` or an `A record` with an IP address).
5. Open a new tab, go to your Namecheap/GoDaddy account, and find **DNS Management** for your new domain.
6. Add the record Render gave you. If it's a CNAME, set the Host as `@` or `www` and the target to your Render URL.
7. Save it. Wait a little while (sometimes up to an hour) for the DNS to propagate.

## HTTPS / SSL Certificate
You don't need to configure HTTPS manually! Render automatically generates your SSL (HTTPS) certificate and renews it for you. As soon as your custom domain is connected and verified, `https://` will work securely.

## Local Development (Testing on your PC)
When you want to add new projects or change the text, test it on your computer first before uploading to GitHub:
1. Open up your terminal in this `simple_app` folder.
2. Install the requirements (only needed once): `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open your web browser and go to: `http://127.0.0.1:8080/`
