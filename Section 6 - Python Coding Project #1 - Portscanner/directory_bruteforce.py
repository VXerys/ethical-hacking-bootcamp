import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

WORDLIST_FILE = "wordlist.txt"
RESULTS_FILE = "scan_results.txt"
NUM_THREADS = 10
TIMEOUT = 5 

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15",
]

def load_wordlist(filename):
    """Muat wordlist dari file dan kembalikan sebagai list."""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def scan_directory(session, base_url, directory):
    """
    Mencoba mengakses direktori dan mengembalikan hasil jika ditemukan.
    """
    if not base_url.endswith("/"):
        base_url += "/"
    
    url = base_url + directory
    
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        response = session.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        if response.status_code in [200, 301, 302, 403]:
            return (url, response.status_code)
    except requests.RequestException:
        pass
    return None

def write_results(results, filename):
    """
    Menulis hasil scanning ke file.
    """
    try:
        with open(filename, "w") as f:
            for url, status in results:
                f.write(f"{url} (Status: {status})\n")
        print(f"[+] Hasil disimpan di {filename}")
    except IOError as e:
        print(f"[ERROR] Tidak dapat menulis ke file {filename}: {e}")

def main():
    target_url = input("Masukkan target URL (misalnya, http://example.com): ").strip()
    if not target_url:
        print("Target URL tidak boleh kosong!")
        return

    directories = load_wordlist(WORDLIST_FILE)
    print(f"[+] Loaded {len(directories)} entries from wordlist.")

    found = []

    with requests.Session() as session:
        with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            future_to_dir = {
                executor.submit(scan_directory, session, target_url, directory): directory 
                for directory in directories
            }
            for future in as_completed(future_to_dir):
                result = future.result()
                if result:
                    url, status = result
                    print(f"[FOUND] {url} (Status: {status})")
                    found.append((url, status))
    
    print(f"[+] Scanning selesai. Ditemukan {len(found)} direktori yang valid.")

    if found:
        write_results(found, RESULTS_FILE)

if __name__ == "__main__":
    main()
