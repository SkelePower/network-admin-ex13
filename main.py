from flask import Flask, render_template, request, redirect, url_for
import get_ip
import get_name
import ping_ip
import ping_scan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/root", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        ip = request.form.get("ip")
        return redirect(url_for("ping", ip=ip))
    else:
        return render_template("root.html", name=get_name.get_computer_name())


@app.route("/ip")
def ip():
    local_ip = get_ip.get_local_ip()
    public_ip = get_ip.get_public_ip()
    return render_template("ip.html", local_ip=local_ip, public_ip=public_ip)


@app.route("/pingip/<ip>")
def ping(ip):
    result = ping_ip.ping_ip(ip)
    return render_template("ping.html", result=result, ip=ip)


@app.route("/activepoints")
def active_points():
    subnet_mask = get_ip.get_subnet_mask()
    local_ip = get_ip.get_local_ip()
    result = ping_scan.ping_scan(local_ip, subnet_mask)
    return render_template("pingscan.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
