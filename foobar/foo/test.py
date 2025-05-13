from . import global_v
# global_v = {}

def run():
    global_v["key"] = "value"
    print global_v

    import bar
    bar.print_global_v()

if __name__ == "__main__":
    global_v["key"] = "value"
    print global_v

    import bar
    bar.print_global_v()