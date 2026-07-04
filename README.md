# Google Indexing API Automation Script

This script automates the process of instantly notifying Google to crawl and index your web pages. Instead of waiting days or weeks for Googlebot to organically find your pages, this tool parses your local `sitemap.xml`, extracts all URLs, and pushes them directly to the Google Indexing API queue for fast-track processing.

---

## 🛠 Prerequisites & Initial Setup

To successfully run this script and bypass the standard `Discovered - currently not indexed` delay, you must link your domain across Google Cloud Platform and Google Search Console.

### Phase 1: Google Cloud Platform (GCP) Configuration

1. **Create a Project:** Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2. **Enable the Indexing API:** Navigate to **APIs & Services > Library**, search for **Web Search Indexing API**, and click **Enable**.
3. **Create a Service Account:** - Go to **APIs & Services > Credentials** (or **IAM & Admin > Service Accounts**).
   - Click **Create Service Account**, give it a name, and proceed to complete creation.
4. **Generate a JSON Key:**
   - Click on your newly created Service Account profile.
   - Switch to the **Keys** tab.
   - Click **Add Key > Create new key** and select **JSON** format.
   - A secure file will be downloaded to your machine. **Rename this file to `service_account.json`** and place it in your root script folder.
5. **Copy the Client Email:** Inside your downloaded JSON file, find and copy the email address associated with the key (e.g., `your-account@your-project.iam.gserviceaccount.com`).

### Phase 2: Google Search Console Setup

1. **Access Search Console:** Open the [Google Search Console](https://search.google.com/search-console) property verified for your target domain.
2. **Navigate to Permissions:** Go to **Settings > Users and permissions**.
3. **Add the Service Account as an Owner:**
   - Click **Add User**.
   - Paste the `client_email` address you copied from the JSON file in Phase 1.
   - **CRITICAL:** Set the Permission level to **Owner** (or Full with verification capabilities). Google's API restricts indexing request submissions strictly to verified domain owners.

---

## 💻 Technical Requirements & Usage

### 1. Installation

Ensure Python is installed on your machine, then execute the following command in your terminal to fetch the official Google authorization dependency:

```bash
pip install google-api-python-client google-auth requests
```

### 2. File Organization

Place all required assets inside a single working directory:

- `indexer.py` — The core automation script.

- `sitemap.xml` — Your localized, updated structure map containing target URLs.

- `service_account.json` — The security key generated from Google Cloud.

### 3. Execution

Launch the automation script from your command prompt/terminal:

```Bash
python indexer.py
```

## ⚠️ Key Notes & Important Reminders

### API Activation Check:

If the terminal yields a `403 Permission Denied (SERVICE_DISABLED)` response on your first run, click the direct link provided in the terminal output payload to verify that the Web Search Indexing API toggle is explicitly switched on for that exact project identifier.

### Daily Quota Limits:

Google provides a generous free tier allowing up to 200 URL submissions per day per service account. If your sitemap exceeds 200 nodes, batch them out across multiple days.

### Intended Scope:

While Google officially limits this API scope to Job Postings and Live Events data structures, it remains highly successful for indexing custom local directories, dynamic service nodes, and programmatic location structures.
