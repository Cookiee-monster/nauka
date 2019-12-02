import re


def parse_markdown(markdown):

    # Definition of searching patterns for regex module
    paterns = {"header": "^(\\#\\#*)",
               "bold_start": "(__)(\\w)|(\\*\\*)(\\w)",
               "bold_end": "(\\w)(__)|(\\w)(\\*\\* )",
               "italic_start": "(_)(\\w)|(\\*)(\\w)",
               "italic_end": "(\\w)(_)|(\\w)(\\* )",
               "list": "^\\* (.*)"}

    # Definition of html tags to use as a result
    html_tags = {"bold_start": "<strong>",
                 "bold_end": "</strong>",
                 "italic_start": "<em>",
                 "italic_end": "</em>"}

    lines = markdown.split('\n')
    res = ''

    # Check whether the list is continued
    in_list = False

    # Going line by line through the input
    for line in lines:

        # Headers
        if re.findall(paterns["header"], line):

            header_counter = len(re.findall(paterns["header"], line)[0])

            # Counts number of # occurrences - to set which header level is it
            # if the value is greater than 0 it means that the proper header level should be used

            line = "<h{}>{}</h{}>".format(header_counter, line[header_counter+1:], header_counter)

        if re.match(paterns["list"], line):
            # Lists
            if not in_list:
                in_list = True
                line = '<ul><li>' + line[2:] + '</li>'
            else:
                line = '<li>' + line[2:] + '</li>'
        else:
            if in_list:
                line = "</ul>" + line
                in_list = False

        # Bold and Italics tags - replacements of the symbols
        line = re.sub(paterns["bold_start"], html_tags["bold_start"]+r"\2", line)
        line = re.sub(paterns["bold_end"], r"\1"+html_tags["bold_end"], line)
        line = re.sub(paterns["italic_start"], html_tags["italic_start"]+r"\2", line)
        line = re.sub(paterns["italic_end"], r"\1"+html_tags["italic_end"], line)

        # Paragraph if no other tag was used before
        if not re.match('<h|<ul|<p|<li', line):
            line = '<p>' + line + '</p>'

        # Adding the line to the result
        res += line

    if in_list:  # Finishing with </ul> tag
        res += '</ul>'
    return res
