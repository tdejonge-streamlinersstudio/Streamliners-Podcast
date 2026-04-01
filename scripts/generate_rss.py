import xml.etree.ElementTree as ET

def generate_rss_feed(title, link, description, items):
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')

    ET.SubElement(channel, 'title').text = title
    ET.SubElement(channel, 'link').text = link
    ET.SubElement(channel, 'description').text = description

    for item in items:
        item_element = ET.SubElement(channel, 'item')
        ET.SubElement(item_element, 'title').text = item['title']
        ET.SubElement(item_element, 'link').text = item['link']
        ET.SubElement(item_element, 'description').text = item['description']
        ET.SubElement(item_element, 'pubDate').text = item['pub_date']

    return ET.tostring(rss, encoding='utf-8', xml_declaration=True).decode()

if __name__ == "__main__":
    title = "Streamliners Podcast"
    link = "http://example.com"
    description = "A podcast about streamlining and efficiency."
    items = [
        {
            'title': 'Episode 1',
            'link': 'http://example.com/episode1',
            'description': 'The first episode of Streamliners.',
            'pub_date': 'Mon, 01 Apr 2026 01:00:00 +0000'
        },
        {
            'title': 'Episode 2',
            'link': 'http://example.com/episode2',
            'description': 'The second episode of Streamliners.',
            'pub_date': 'Mon, 01 Apr 2026 02:00:00 +0000'
        }
    ]

    rss_feed = generate_rss_feed(title, link, description, items)
    print(rss_feed)