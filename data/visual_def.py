import xml.etree.ElementTree as ET


def text_len(sql_input):
    sql_output = ''
    for i in sql_input:
        sql_output += i.replace('\\n','\n') + '\n--\n'
    return sql_output


def config_read(find_attrib):
    tree = ET.parse(r'./config.xml')
    root = tree.getroot()
    for child in root:
        if child.attrib['name'] == find_attrib:
            return child.text


def config_update(find_attrib, update_value):
    tree = ET.parse(r'./config.xml')
    root = tree.getroot()
    for child in root:
        if child.attrib['name'] == find_attrib:
            child.text = str(update_value)
    new_tree = ET.tostring(root, encoding='unicode', method='xml')
    new_tree = str(new_tree).encode().decode('UTF-8')
    new_root = open(r'./config.xml', 'w', encoding="utf-8")
    new_root.write(new_tree)