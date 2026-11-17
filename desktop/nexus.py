import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress, json, base64, re
class Nexus(tk.Tk):
 def __init__(self):
  super().__init__(); self.title("NEXUS Engineering Suite"); self.geometry("850x650"); self.minsize(650,500); self.configure(bg="#0b1020")
  style=ttk.Style(self); style.theme_use("clam"); style.configure(".",background="#111a2d",foreground="#edf4ff",fieldbackground="#091222"); style.configure("TButton",padding=8); style.configure("TLabel",background="#0b1020",foreground="#edf4ff")
  ttk.Label(self,text="NEXUS ENGINEERING SUITE",font=("Segoe UI",22,"bold")).pack(pady=18)
  ttk.Label(self,text="Offline engineering workbench • Software • Electronics • Networking").pack()
  tabs=ttk.Notebook(self); tabs.pack(fill="both",expand=True,padx=18,pady=18)
  self.tab_ohm(tabs); self.tab_net(tabs); self.tab_json(tabs); self.tab_base64(tabs); self.tab_regex(tabs)
 def page(self,tabs,name):
  f=ttk.Frame(tabs,padding=18); tabs.add(f,text=name); return f
 def entry(self,parent,label,default=""):
  ttk.Label(parent,text=label).pack(anchor="w",pady=(8,2)); e=ttk.Entry(parent,width=70); e.insert(0,default); e.pack(fill="x"); return e
 def result(self,parent):
  t=tk.Text(parent,height=8,bg="#091222",fg="#69e0a5",insertbackground="white",wrap="word"); t.pack(fill="both",expand=True,pady=10); return t
 def tab_ohm(self,tabs):
  f=self.page(tabs,"Ohm's Law"); v=self.entry(f,"Voltage (V)"); i=self.entry(f,"Current (A)"); r=self.entry(f,"Resistance (ohms)"); o=self.result(f)
  def calc():
   try:
    if v.get() and i.get(): V=float(v.get()); I=float(i.get()); R=V/I
    elif v.get() and r.get(): V=float(v.get()); R=float(r.get()); I=V/R
    elif i.get() and r.get(): I=float(i.get()); R=float(r.get()); V=I*R
    else: raise ValueError("Enter any two values.")
    o.delete("1.0","end"); o.insert("end",f"Voltage: {V:g} V\\nCurrent: {I:g} A\\nResistance: {R:g} Ω\\nPower: {V*I:g} W")
   except Exception as e: messagebox.showerror("Calculation",str(e))
  ttk.Button(f,text="Calculate",command=calc).pack(anchor="w")
 def tab_net(self,tabs):
  f=self.page(tabs,"Subnet"); e=self.entry(f,"IPv4 / CIDR","192.168.1.10/24"); o=self.result(f)
  def calc():
   try:
    n=ipaddress.ip_interface(e.get()).network; o.delete("1.0","end"); o.insert("end",f"Network: {n.network_address}/{n.prefixlen}\\nMask: {n.netmask}\\nBroadcast: {n.broadcast_address}\\nHosts: {n.num_addresses}")
   except Exception as x: messagebox.showerror("Subnet",str(x))
  ttk.Button(f,text="Calculate",command=calc).pack(anchor="w")
 def tab_json(self,tabs):
  f=self.page(tabs,"JSON"); a=self.result(f); a.insert("end",'{"nexus":true,"tools":["JSON","Subnet"]}')
  def fmt():
   try: data=json.loads(a.get("1.0","end")); a.delete("1.0","end"); a.insert("end",json.dumps(data,indent=2,ensure_ascii=False))
   except Exception as e: messagebox.showerror("JSON",str(e))
  ttk.Button(f,text="Format / Validate",command=fmt).pack(anchor="w")
 def tab_base64(self,tabs):
  f=self.page(tabs,"Base64"); a=self.entry(f,"Text or Base64"); o=self.result(f)
  def run(mode):
   try:
    raw=a.get().encode() if mode=="encode" else base64.b64decode(a.get(),validate=True); val=base64.b64encode(raw).decode() if mode=="encode" else raw.decode("utf-8")
    o.delete("1.0","end"); o.insert("end",val)
   except Exception as e: messagebox.showerror("Base64",str(e))
  ttk.Button(f,text="Encode",command=lambda:run("encode")).pack(anchor="w"); ttk.Button(f,text="Decode",command=lambda:run("decode")).pack(anchor="w",pady=4)
 def tab_regex(self,tabs):
  f=self.page(tabs,"Regex"); p=self.entry(f,"Pattern",r"\\bNEXUS\\b"); s=self.entry(f,"Test text","NEXUS Engineering Suite"); o=self.result(f)
  def run():
   try:
    m=list(re.finditer(p.get(),s.get())); o.delete("1.0","end"); o.insert("end","\\n".join(f"{x.group()} at {x.start()}" for x in m) or "No matches.")
   except Exception as e: messagebox.showerror("Regex",str(e))
  ttk.Button(f,text="Test",command=run).pack(anchor="w")
if __name__=="__main__": Nexus().mainloop()
