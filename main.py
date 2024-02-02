import requests
from bs4 import BeautifulSoup

def extract_episode_info(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取name="description"节目详情
    description = soup.find('meta', attrs={'name': 'description'})['content']

    # 提取title
    title = soup.title.string

    # 提取og:audio内容
    og_audio_tag = soup.find('meta', attrs={'property': 'og:audio'})
    og_audio_content = og_audio_tag['content'] if og_audio_tag else None

    return title, description, og_audio_content

def download_audio(title, audio_url):
    response = requests.get(audio_url)
    if response.status_code == 200:
        with open(f"{title}.m4a", 'wb') as f:
            f.write(response.content)
        print("音频文件下载成功")
    else:
        print("下载失败，HTTP状态码:", response.status_code)

if __name__ == "__main__":
    url = "https://www.xiaoyuzhoufm.com/episode/65510930d0028fb4cb289db5"
    title, description, og_audio_content = extract_episode_info(url)
    print("节目标题:", title)
    print("节目详情:", description)
    print("音频链接:", og_audio_content)
    download_audio(title, og_audio_content)
