# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "plotly==6.7.0",
#     "pandas==3.0.2",
#     "numpy==2.4.4",
#     "ty==0.0.29",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium", layout_file="layouts/mlh_demo.slides.json")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from pathlib import Path
    import base64

    return Path, base64, mo


@app.cell(hide_code=True)
def _(Path, base64, mo):
    _IMG = Path(__file__).parent / "imgs"

    def _b64(name):
        return base64.b64encode((_IMG / f"{name}.png").read_bytes()).decode()

    def img(name, **kw):
        return mo.image(src=(_IMG / f"{name}.png").read_bytes(), **kw)

    def img_html(name, width=None, extra_style=""):
        w = f'width="{width}"' if width else 'style="width:100%"'
        return (
            f'<img src="data:image/png;base64,{_b64(name)}" {w} '
            f'style="border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.08);{extra_style}" />'
        )

    def gif_html(name, width=None, extra_style=""):
        _b = base64.b64encode((_IMG / f"{name}.gif").read_bytes()).decode()
        w = f'width="{width}"' if width else 'style="max-width:100%"'
        return (
            f'<img src="data:image/gif;base64,{_b}" {w} '
            f'style="border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.12);{extra_style}" />'
        )

    def desktop_img_html(name, width=None, extra_style=""):
        _b = base64.b64encode((_IMG / f"{name}.png").read_bytes()).decode()
        w = f'width="{width}"' if width else 'style="width:100%"'
        return (
            f'<img src="data:image/png;base64,{_b}" {w} '
            f'style="border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,0.08);{extra_style}" />'
        )

    _CARD = (
        "background:#f8f9fb;border-radius:12px;padding:20px 32px;"
        "border:1px solid #eaeaea;max-width:640px;margin:0 auto;"
        "font-size:1.05em;line-height:1.7"
    )

    def stat_card(html):
        return mo.md(f'<div style="{_CARD}">{html}</div>')

    def badge(n, label="points"):
        return (
            f'<span style="color:#1C7362;font-weight:700;font-size:1.1em;">'
            f'{n} {label} selected</span>'
        )

    _HINT = (
        '<div style="text-align:center;color:#ccc;font-size:0.95em;'
        'padding:12px 0;letter-spacing:0.02em;">'
        'Box-select or click &rarr; see statistics</div>'
    )

    def no_sel():
        return mo.md(_HINT)

    return badge, desktop_img_html, gif_html, img_html, no_sel, stat_card


@app.cell(hide_code=True)
def _():
    import plotly.express as px
    import plotly.graph_objects as go
    import pandas as pd
    import numpy as np

    return go, np, pd, px


@app.cell(hide_code=True)
def _(img_html, mo):
    mo.md(f"""
    <div style="text-align:center;">
    <div style="display:flex;justify-content:center;align-items:center;gap:52px;margin-bottom:44px;">
        {img_html("marimo-logo", width=150)}
        {img_html("gresearch-logo", width=150)}
        {img_html("mlh-logo", width=110, extra_style="box-shadow:none;")}
    </div>
    <div style="font-size:2.8em;font-weight:700;color:#1a1a2e;letter-spacing:-0.02em;line-height:1.1;">
        Final Demo
    </div>
    <div style="font-size:1.15em;color:#999;margin-top:20px;letter-spacing:0.04em;">
        Axel Diaz
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    get_n, set_n = mo.state(5, allow_self_loops=True)
    return get_n, set_n


@app.cell(hide_code=True)
def _(get_n, mo, set_n):
    _n = get_n()
    _squares = [i**2 for i in range(1, _n + 1)]
    _slider = mo.ui.slider(1, 20, value=_n, on_change=set_n, label="**Pick a number**", full_width=True)
    mo.vstack([
        mo.md("""
    <div style="text-align:center;margin-bottom:28px;">
    <div style="font-size:1.8em;font-weight:600;color:#1a1a2e;margin-bottom:10px;">What is marimo?</div>
    </div>
    """),
        _slider,
        mo.md(f"""
    <div style="max-width:480px;margin:24px auto 0;background:#f8f9fb;border-radius:14px;
            padding:24px 32px;border:1px solid #eaeaea;text-align:center;">
    <div style="color:#888;font-size:0.95em;margin-bottom:8px;">
        From 1 to <strong style="color:#1a1a2e;">{_n}</strong>
    </div>
    <div style="font-family:'SF Mono','Fira Code',monospace;font-size:1.05em;color:#2d2d2d;
                word-break:break-all;margin-bottom:12px;">
        {', '.join(str(s) for s in _squares)}
    </div>
    <div style="font-size:1.5em;font-weight:700;color:#1C7362;">
        Sum = {sum(_squares)}
    </div>
    </div>
    """),
    ], gap="1rem")
    return


@app.cell(hide_code=True)
def _(img_html, mo):
    _prs = [8291, 8334, 8332, 8440]
    _grid = "\n".join(img_html(str(pr)) for pr in _prs)
    mo.md(f"""
    <div style="text-align:center;margin-bottom:18px;">
    <div style="font-size:1.6em;font-weight:600;color:#1a1a2e;">Contributions</div>
    <div style="font-size:1.05em;color:#888;">Warm Up</div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:1100px;margin:0 auto;">
    {_grid}
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    <div style="text-align:center;">
    <div style="font-size:2em;font-weight:700;color:#1a1a2e;">Reactive Plotly Charts</div>
    <div style="font-size:1.1em;color:#888;margin-top:8px;">
        10 chart types with selection-driven reactivity
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo, px):
    _df_sc = px.data.iris()
    _fig_sc = px.scatter(
        _df_sc, x="sepal_width", y="sepal_length", color="species",
        render_mode="webgl", template="plotly_white",
        color_discrete_sequence=["#1C7362", "#E8804C", "#5B8DB8"],
    )
    _fig_sc.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    _fig_sc.update_traces(marker=dict(size=8, opacity=0.8))
    scatter_chart = mo.ui.plotly(_fig_sc)
    return (scatter_chart,)


@app.cell(hide_code=True)
def _(badge, img_html, mo, no_sel, pd, scatter_chart, stat_card):
    _sel = scatter_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Sepal length: <strong>{_df['y'].mean():.2f}</strong> avg "
            f"&nbsp;&middot;&nbsp; range {_df['y'].min():.1f}–{_df['y'].max():.1f}<br/>"
            f"Sepal width: <strong>{_df['x'].mean():.2f}</strong> avg "
            f"&nbsp;&middot;&nbsp; range {_df['x'].min():.1f}–{_df['x'].max():.1f}"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("8490", width=600)), scatter_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, px):
    _df_hi = px.data.tips()
    _fig_hi = px.histogram(
        _df_hi, x="total_bill", nbins=25, template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_hi.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    hist_chart = mo.ui.plotly(_fig_hi)
    return (hist_chart,)


@app.cell(hide_code=True)
def _(badge, hist_chart, img_html, mo, no_sel, pd, stat_card):
    _sel = hist_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _v = _df["x"]
        _pct = len(_sel) / 244 * 100
        _stats = stat_card(
            f"{badge(len(_sel), 'bills')} &nbsp;&middot;&nbsp; {_pct:.0f}% of dataset<br/>"
            f"Range: <strong>${_v.min():.2f}</strong> – <strong>${_v.max():.2f}</strong><br/>"
            f"Mean: <strong>${_v.mean():.2f}</strong> &nbsp;&middot;&nbsp; Std: ${_v.std():.2f}"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("8489", width=600)), hist_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, np, pd, px):
    np.random.seed(42)
    _dates_ln = pd.date_range("2024-01-01", periods=120, freq="D")
    _prices_ln = (100 + np.cumsum(np.random.randn(120) * 1.5)).round(2)
    _df_ln = pd.DataFrame({"date": _dates_ln, "price": _prices_ln})
    _fig_ln = px.line(
        _df_ln, x="date", y="price", template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_ln.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    line_chart = mo.ui.plotly(_fig_ln)
    return (line_chart,)


@app.cell(hide_code=True)
def _(badge, img_html, line_chart, mo, no_sel, pd, stat_card):
    _sel = line_chart.value
    _df = pd.DataFrame(_sel) if _sel else None
    if _df is not None and "y" in _df.columns and len(_df) >= 2:
        _s, _e = _df["y"].iloc[0], _df["y"].iloc[-1]
        _ret = ((_e - _s) / _s) * 100
        _col = "#1C7362" if _ret >= 0 else "#E74C3C"
        _d0, _d1 = str(_df["x"].iloc[0])[:10], str(_df["x"].iloc[-1])[:10]
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Period: {_d0} &rarr; {_d1}<br/>"
            f"Return: <strong style='color:{_col}'>{_ret:+.1f}%</strong> "
            f"&nbsp;&middot;&nbsp; ${_s:.2f} &rarr; ${_e:.2f}"
        )
    elif _df is not None and "y" in _df.columns:
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Price: <strong>${_df['y'].iloc[0]:.2f}</strong>"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("8657", width=600)), line_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, pd, px):
    _df_bar = pd.DataFrame({
        "product": ["Electronics", "Clothing", "Food", "Books", "Sports", "Home"],
        "revenue": [42000, 31000, 28000, 15000, 22000, 19000],
    })
    _fig_bar = px.bar(
        _df_bar, x="product", y="revenue", template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_bar.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    bar_chart = mo.ui.plotly(_fig_bar)
    return (bar_chart,)


@app.cell(hide_code=True)
def _(badge, bar_chart, img_html, mo, no_sel, pd, stat_card):
    _sel = bar_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _total = 157000
        _rev = _df["y"].sum()
        _pct = (_rev / _total) * 100
        _cats = ", ".join(str(c) for c in _df["x"].tolist())
        _stats = stat_card(
            f"{badge(len(_sel), 'categories')}<br/>"
            f"{_cats}<br/>"
            f"Revenue: <strong>${_rev:,.0f}</strong> &nbsp;&middot;&nbsp; "
            f"<strong>{_pct:.0f}%</strong> of total"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("8787", width=600)), bar_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(go, mo):
    _fig_wf = go.Figure(go.Waterfall(
        x=["Revenue", "COGS", "Gross Profit", "OpEx", "Tax", "Net Income"],
        y=[480, -180, 300, -120, -45, 135],
        measure=["absolute", "relative", "total", "relative", "relative", "total"],
        connector={"line": {"color": "#ccc"}},
        increasing={"marker": {"color": "#1C7362"}},
        decreasing={"marker": {"color": "#E74C3C"}},
        totals={"marker": {"color": "#5B8DB8"}},
    ))
    _fig_wf.update_layout(
        dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16),
        template="plotly_white", showlegend=False,
    )
    wf_chart = mo.ui.plotly(_fig_wf)
    return (wf_chart,)


@app.cell(hide_code=True)
def _(badge, img_html, mo, no_sel, pd, stat_card, wf_chart):
    _sel = wf_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _net = _df["y"].sum()
        _col = "#1C7362" if _net >= 0 else "#E74C3C"
        _items = ", ".join(str(x) for x in _df["x"].tolist())
        _stats = stat_card(
            f"{badge(len(_sel), 'items')}<br/>"
            f"{_items}<br/>"
            f"Net impact: <strong style='color:{_col}'>${_net:+,.0f}K</strong>"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9045", width=600)), wf_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(go, mo, px):
    _df_vi = px.data.tips()
    _fig_vi = go.Figure(go.Violin(
        x=_df_vi["day"],
        y=_df_vi["total_bill"],
        customdata=_df_vi[["tip", "size", "sex"]].values,
        points="all",
        jitter=0.3,
        pointpos=0,
        box_visible=True,
        meanline_visible=True,
        marker=dict(size=6, opacity=0.65, color="#1C7362"),
        line=dict(color="#1C7362"),
        fillcolor="rgba(28,115,98,0.18)",
        hovertemplate=(
            "day=%{x}<br>bill=$%{y:.2f}<br>"
            "tip=$%{customdata[0]:.2f}<extra></extra>"
        ),
        name="total_bill",
    ))
    _fig_vi.update_layout(
        dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16),
        template="plotly_white", showlegend=False,
        xaxis_title="Day", yaxis_title="Total Bill ($)",
    )
    violin_chart = mo.ui.plotly(_fig_vi)
    return (violin_chart,)


@app.cell(hide_code=True)
def _(badge, img_html, mo, no_sel, pd, stat_card, violin_chart):
    _sel = violin_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _by_day = _df.groupby("x")["y"].agg(count="count", mean="mean")
        _day_lines = " &nbsp;&middot;&nbsp; ".join(
            f"<strong>{d}</strong>: {int(r['count'])} pts (avg ${r['mean']:.2f})"
            for d, r in _by_day.iterrows()
        )
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"{_day_lines}<br/>"
            f"Overall avg: <strong>${_df['y'].mean():.2f}</strong> "
            f"&nbsp;&middot;&nbsp; Std: ${_df['y'].std():.2f}"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9011", width=600)), violin_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, np, pd, px):
    np.random.seed(7)
    _dates_ar = pd.date_range("2024-01-01", periods=90, freq="D")
    _users_ar = np.cumsum(np.random.poisson(8, 90))
    _df_ar = pd.DataFrame({"date": _dates_ar, "active_users": _users_ar})
    _fig_ar = px.area(
        _df_ar, x="date", y="active_users", template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_ar.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    area_chart = mo.ui.plotly(_fig_ar)
    return (area_chart,)


@app.cell(hide_code=True)
def _(area_chart, badge, img_html, mo, no_sel, pd, stat_card):
    _sel = area_chart.value
    _df = pd.DataFrame(_sel) if _sel else None
    if _df is not None and "y" in _df.columns and len(_df) >= 2:
        _s, _e = _df["y"].iloc[0], _df["y"].iloc[-1]
        _g = _e - _s
        _pct = (_g / max(_s, 1)) * 100
        _d0, _d1 = str(_df["x"].iloc[0])[:10], str(_df["x"].iloc[-1])[:10]
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Period: {_d0} &rarr; {_d1}<br/>"
            f"Users: {_s:,} &rarr; {_e:,} "
            f"&nbsp;&middot;&nbsp; Growth: <strong style='color:#1C7362'>+{_g:,} ({_pct:.0f}%)</strong>"
        )
    elif _df is not None and "y" in _df.columns:
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Users: <strong>{int(_df['y'].iloc[0]):,}</strong> on {str(_df['x'].iloc[0])[:10]}"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9046", width=600)), area_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(go, mo, px):
    _df_bx = px.data.tips()
    _fig_bx = go.Figure(go.Box(
        x=_df_bx["day"],
        y=_df_bx["tip"],
        customdata=_df_bx[["total_bill", "size", "sex"]].values,
        boxpoints="all",
        jitter=0.3,
        pointpos=0,
        marker=dict(size=6, opacity=0.65, color="#1C7362"),
        line=dict(color="#1C7362"),
        fillcolor="rgba(28,115,98,0.18)",
        hovertemplate=(
            "day=%{x}<br>tip=$%{y:.2f}<br>"
            "bill=$%{customdata[0]:.2f}<extra></extra>"
        ),
        name="tip",
    ))
    _fig_bx.update_layout(
        dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16),
        template="plotly_white", showlegend=False,
        xaxis_title="Day", yaxis_title="Tip ($)",
    )
    box_chart = mo.ui.plotly(_fig_bx)
    return (box_chart,)


@app.cell(hide_code=True)
def _(badge, box_chart, img_html, mo, no_sel, pd, stat_card):
    _sel = box_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _v = _df["y"]
        _q1, _q3 = _v.quantile(0.25), _v.quantile(0.75)
        _by_day = _df.groupby("x")["y"].mean()
        _day_cmp = " &nbsp;&middot;&nbsp; ".join(
            f"<strong>{d}</strong>: ${m:.2f}" for d, m in _by_day.items()
        )
        _stats = stat_card(
            f"{badge(len(_sel), 'tips')}<br/>"
            f"Per day &mdash; {_day_cmp}<br/>"
            f"Mean: <strong>${_v.mean():.2f}</strong> "
            f"&nbsp;&middot;&nbsp; Median: ${_v.median():.2f} "
            f"&nbsp;&middot;&nbsp; IQR: ${_q3 - _q1:.2f}"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9010", width=600)), box_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, px):
    _df_st = px.data.tips()
    _fig_st = px.strip(
        _df_st, x="day", y="total_bill", template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_st.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    strip_chart = mo.ui.plotly(_fig_st)
    return (strip_chart,)


@app.cell(hide_code=True)
def _(badge, img_html, mo, no_sel, pd, stat_card, strip_chart):
    _sel = strip_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        _v = _df["y"]
        _by_day = _df.groupby("x")["y"].mean()
        _day_avg = " &nbsp;&middot;&nbsp; ".join(
            f"<strong>{d}</strong>: ${m:.2f}" for d, m in _by_day.items()
        )
        _stats = stat_card(
            f"{badge(len(_sel))}<br/>"
            f"Avg bill per day &mdash; {_day_avg}<br/>"
            f"Overall avg: <strong>${_v.mean():.2f}</strong> "
            f"&nbsp;&middot;&nbsp; Total: <strong>${_v.sum():,.2f}</strong>"
        )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9012", width=600)), strip_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(mo, pd, px):
    _df_fn = pd.DataFrame({
        "stage": ["Leads", "Qualified", "Proposal", "Negotiation", "Closed Won"],
        "count": [1200, 720, 440, 210, 85],
    })
    _fig_fn = px.funnel(
        _df_fn, x="count", y="stage", template="plotly_white",
        color_discrete_sequence=["#1C7362"],
    )
    _fig_fn.update_layout(dragmode="select", clickmode="event+select", height=340, margin=dict(t=16, b=16))
    funnel_chart = mo.ui.plotly(_fig_fn)
    return (funnel_chart,)


@app.cell(hide_code=True)
def _(badge, funnel_chart, img_html, mo, no_sel, pd, stat_card):
    _sel = funnel_chart.value
    if _sel:
        _df = pd.DataFrame(_sel)
        if len(_df) > 1:
            _f, _l = _df["x"].iloc[0], _df["x"].iloc[-1]
            _conv = (_l / _f) * 100
            _stages = f'{_df["y"].iloc[0]} &rarr; {_df["y"].iloc[-1]}'
            _stats = stat_card(
                f"{badge(len(_sel), 'stages')}<br/>"
                f"{_stages}<br/>"
                f"Conversion: <strong>{_conv:.1f}%</strong> "
                f"&nbsp;&middot;&nbsp; {_f:,} &rarr; {_l:,}"
            )
        else:
            _stats = stat_card(
                f"{badge(1, 'stage')}<br/>"
                f"<strong>{_df['y'].iloc[0]}</strong>: {_df['x'].iloc[0]:,}"
            )
    else:
        _stats = no_sel()
    mo.vstack([mo.md(img_html("9044", width=600)), funnel_chart, _stats], align="center", gap="0.75rem")
    return


@app.cell(hide_code=True)
def _(img_html, mo):
    mo.md(f"""
    <div style="text-align:center;margin-bottom:18px;">
    <div style="font-size:1.6em;font-weight:600;color:#1a1a2e;">Plotly — Bug Fixes &amp; Enhancements</div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:1100px;margin:0 auto;">
    {img_html("8782")}
    {img_html("8685")}
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(img_html, mo):
    mo.md(f"""
    <div style="display:flex;flex-direction:column;align-items:center;gap:20px;">
    <div style="text-align:center;margin-bottom:4px;">
    <div style="font-size:1.6em;font-weight:600;color:#1a1a2e;">Ty LSP Fix</div>
    </div>
    {img_html("8390", width=620)}
    {img_html("ty-lsp-props", width=620)}
    </div>
    """)
    return


@app.cell
def _():
    a: int = 10
    b: int = 5
    return


@app.cell(hide_code=True)
def _(gif_html, img_html, mo):
    mo.md(f"""
    <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;">
    {img_html("8893", width=700)}
    {gif_html("pre", width=860)}
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(gif_html, mo):
    mo.md(f"""
    <div style="display:flex;align-items:center;justify-content:center;height:100%;">
    {gif_html("post", width=860)}
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    <div style="text-align:center;">
    <div style="font-size:2.6em;font-weight:700;color:#1a1a2e;letter-spacing:-0.02em;">
        Reflections and Thanks
    </div>
    <div style="font-size:1.15em;color:#999;margin-top:14px;letter-spacing:0.02em;">
        Marimo team &middot; G-Research &middot; MLH
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(desktop_img_html, mo):
    mo.md(f"""
    <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;">
    {desktop_img_html("questions", width=520)}
    <div style="font-size:2em;font-weight:600;color:#1a1a2e;">
        Any questions?
    </div>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
