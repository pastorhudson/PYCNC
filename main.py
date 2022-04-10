def get_input():
    coords = {
        'x': float(input("Enter 'X' Value: ")),
        # 'y': int(input("Enter 'Y' Value: ")),
        'radius': float(input("Enter Radius Value: ")),
        'step': float(input("Enter Step Value: ")),
        'last_step': 0,
        'depth': float(input("Enter Depth Value as Negative Number: "))
    }
    return coords


def run(coords):
        with open('tornado_mill.txt', 'a') as f:

            while coords['last_step'] > coords['depth']:
                line = "".join(["G03",
                                f"X{coords['x'] - coords['radius']}",
                                "R",
                                f"{coords['radius']}",
                                f"Z{round(coords['last_step'] - coords['step'], 4)}",
                                ]
                               )

                coords['last_step'] = coords['last_step'] - coords['step']
                # print(coords)
                line += "\n" + "".join(["G03",
                                        f"X{coords['x'] + coords['radius']}",
                                        "R",
                                        f"{coords['radius']}",
                                        f"Z{round(coords['last_step'] - coords['step'], 4)}\n",
                                        ])

                coords['last_step'] = coords['last_step'] - coords['step']
                print(line)
                f.write(line)


if __name__ == "__main__":
    coords = get_input()
    run(coords)
