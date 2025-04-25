def count_char_occurrences(text):
    from collections import Counter
    filtered = (char.lower() for char in text if char.isalpha())
    return dict(Counter(filtered))


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted


def dict_to_table(data_dict, columns):
    columns_upper = [col.upper() for col in columns]
    rows = []

    for entry in data_dict.values():
        row = []
        for col in columns:
            row.append(str(entry.get(col, "N/A")))
        rows.append(row)

    col_widths = [max(len(columns_upper[i]), *(len(row[i]) for row in rows)) for i in range(len(columns))]

    header = "| " + " | ".join(columns_upper[i].ljust(col_widths[i]) for i in range(len(columns))) + " |"
    separator = "|-" + "-|-".join("-" * col_widths[i] for i in range(len(columns))) + "-|"

    row_lines = []
    for row in rows:
        line = "| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(columns))) + " |"
        row_lines.append(line)

    return "\n".join([header, separator] + row_lines)


def deep_update(base_dict, update_dict):
    def recursive_update(base, update):
        result = base.copy()
        for k in update:
            if k in base:
                if isinstance(base[k], dict) and isinstance(update[k], dict):
                    result[k] = recursive_update(base[k], update[k])
                else:
                    result[k] = update[k]
        return result
    return recursive_update(base_dict, update_dict)
