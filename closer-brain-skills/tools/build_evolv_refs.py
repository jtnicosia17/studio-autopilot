import json,sys,os
src,out=sys.argv[1],sys.argv[2]
g=json.load(open(os.path.join(src,"governed.json"))); l=json.load(open(os.path.join(src,"library.json")))
L=[]
w=L.append
w("# EVOLV product knowledge (for sales calls)\n")
w(f"Source: EVOLV Source Brain, release **{g['release']}**. Prices in CAD. When this file and the live Source Brain disagree, the Source Brain wins.\n")
w("## Contents\n1. Offer & pricing rules\n2. Goal → recommended protocol\n3. Product catalogue (price, dose, schedule)\n4. How to talk about each compound\n5. Recent updates\n6. Links\n")
c=g["commercial"]
w("## 1. Offer & pricing rules\n")
w(f"- **Current policy:** {c['Policy']}")
w(f"- 12-Week Best Value: exact-SKU 3-pack saves {int(c['3-pack peptide SKU savings']*100)}%, 5-pack {int(c['5-pack peptide SKU savings']*100)}%, then {int(c['Align 12-Week Best Value discount']*100)}% off; Interac e-transfer adds {int(c['Interac additional savings']*100)}% more.")
w(f"- Monthly / 4-week purchases: regular price, no pack savings; Interac saves {int(c['Monthly Interac additional savings']*100)}%.")
w(f"- Free shipping at ${c['Free shipping threshold']}+ after discounts, otherwise ${c['Shipping below threshold']}. No HST.")
w(f"- Bacteriostatic water: 10 mL bottle ${c['BAC Water 10 mL price']} (only 10 mL is used).")
w("- **Sales angle (Hormozi step-down):** lead with the 12-Week Best Value plan as the anchor, then Interac for the extra savings, then monthly/phase purchases as the step-down. Never discount outside these rules.\n")
w("## 2. Goal → recommended protocol\n")
for r in g["recommendations"]:
    if r.get("Status","Active")!="Active": continue
    w(f"### {r['Goal']}\n- **First choice:** {r.get('First Choice','—')}\n- **Second / support:** {r.get('Second Choice / Support','—')}\n- **Other options:** {r.get('Additional Preferred Options','—')}\n- {r.get('Selection Instruction','')}\n")
w("## 3. Product catalogue\n")
w("| Product (SKU) | Form | Price | Dose | Timing / frequency | Days | Cycle |\n|---|---|---|---|---|---|---|")
for s in g["standards"]:
    if s.get("status")!="Active": continue
    price=f"${s['price']:.2f}" if isinstance(s.get("price"),(int,float)) else "—"
    w(f"| {s.get('product') or s['name']} ({s.get('sku') or '—'}) | {s['form']}{' (pen)' if s.get('pen') else ''} | {price} | {s.get('doseSummary') or s.get('measureSummary') or '—'} | {s.get('timing') or '—'} · {s.get('frequency') or '—'} | {s.get('days') or '—'} | {s.get('cycle') or '—'} |")
w("\nFull phase-by-phase dosing (units, titration, holds) is in `evolv-protocol-cheatsheet.md`.\n")
w("## 4. How to talk about each compound\n")
w("Use the *client-facing wording* on calls. It is EVOLV's own approved language, so it's what the closer can say with certainty. The *don't claim* line is EVOLV's boundary for that compound.\n")
for name,e in g["education"].items():
    w(f"### {name}")
    w(f"- **What it is:** {e.get('Approved educational summary','')}")
    w(f"- **Say:** {e.get('Permitted client-facing wording','')}")
    w(f"- **Evidence level:** {e.get('Evidence classification','')}")
    w(f"- **Don't claim:** {e.get('Claims not permitted','')}\n")
w("## 5. Recent updates\n")
for u in g["updates"]: w(f"- {u}")
w("\n## 6. Links\n")
for k,v in g["links"].items(): w(f"- {k}: {v}")
open(os.path.join(out,"evolv-knowledge.md"),"w").write("\n".join(L)+"\n")
def doc(ids,title,fn,intro):
    D=[f"# {title}\n",intro+"\n"]
    for i in ids:
        d=next(x for x in l["docs"] if x["id"]==i)
        D.append(f"\n## {d['title']} (v{d.get('version','')})\n")
        last=None
        for ch in [c for c in l["chunks"] if c["doc"]==i]:
            if ch["sec"]!=last: D.append(f"\n### {ch['sec']}\n"); last=ch["sec"]
            D.append(ch["text"].strip()+"\n")
    open(os.path.join(out,fn),"w").write("\n".join(D))
doc(["15","17"],"EVOLV protocol cheat sheet","evolv-protocol-cheatsheet.md","Exact products, preparation, phase-by-phase doses and pen dosing from the EVOLV Source Brain. Use it to answer 'how do I take it / how long / how many vials' questions on a call. Read only the section for the compound you need.")
doc(["18","05","U6"],"EVOLV consult & investment process","evolv-sales-process.md","How EVOLV runs the consultation intake and presents the investment summary, plus the owner's discount policy. Use it to fit the call flow to EVOLV's process.")
