import cv2


def draw_vips(frame, vips, padding=5):
    for vip_info in vips:
        box = vip_info['box']
        name = vip_info['name']
        x0, y0, w, h = box
        x1, y1 = x0 + w, y0 + h
        if padding:
            size = max(x1 - x0, y1 - y0)
            xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
            x0, y0 = xm - size / 2 - padding, ym - size / 2 - padding
            x1, y1 = xm + size / 2 + padding, ym + size / 2 + padding
        x0, y0, x1, y1 = list(map(int, [x0, y0, x1, y1]))
        cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 255, 255), 1)
        cv2.putText(frame, name, (x0 + 2, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 1)


def display_fps(frame, fps):
    cv2.putText(
        frame, "FPS: {:.2f}".format(fps),
        (20, 30), cv2.FONT_HERSHEY_SIMPLEX, .7, (51, 28, 204), 1
    )
