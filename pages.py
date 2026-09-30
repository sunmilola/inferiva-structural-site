"""Page content. One function per page, so copy lives apart from the shell."""


def build(page, head, nextlinks, icon, opsmap):
    # ======================================================================
    # HOME
    # ======================================================================
    page("index.html", "One risk. One operating platform.",
         "Your institution carries one financial-crime exposure. INFERIVA connects AML, fraud, customer risk, investigations, reporting and agent supervision in one governed environment.",
         """
<header class="hero"><div class="wrap"><div class="hgrid">
  <div>
    <div class="rule-accent"></div>
    <h1>One risk.<br>One operating platform.</h1>
    <p class="lede">Your institution carries one financial-crime exposure.
    Why manage it through disconnected systems?</p>
    <div class="btns">
      <a class="btn" href="company/contact.html">Arrange an executive briefing</a>
      <a class="btn ghost" href="start/diagnostic.html">Start with a diagnostic</a>
    </div>
  </div>
  <div>""" + opsmap() + """</div>
</div></div></header>

<section class="sec"><div class="wrap">
  <div class="split" style="margin-top:0">
    <div>
      <h2 class="head">A unified financial-crime operating platform</h2>
      <p class="lead">INFERIVA connects the institution's financial-crime operations
      in one governed environment — from detection and customer risk through
      investigation, decision, reporting, evidence and improvement.</p>
      <p class="lead">Not six products sharing a login. <strong>One record, one
      decision trail, one account of what the institution actually did.</strong></p>
    </div>
    <div>
      <p class="crumb" style="color:var(--soft);letter-spacing:.14em;font-weight:600;
      font-size:12.5px;margin:0 0 14px">CONNECTED OPERATIONS</p>
      <div class="ops">
        <div class="opitem"><a href="platform/aml.html">""" + icon("aml", True) + """
          <span><b>AML</b><span>Detection, scenarios and thresholds you can defend</span></span></a></div>
        <div class="opitem"><a href="platform/fraud.html">""" + icon("fraud", True) + """
          <span><b>Fraud</b><span>Interdiction before the money leaves</span></span></a></div>
        <div class="opitem"><a href="platform/customer-risk.html">""" + icon("customer", True) + """
          <span><b>Customer risk</b><span>Who they are, and what that means afterwards</span></span></a></div>
        <div class="opitem"><a href="platform/investigations.html">""" + icon("investigations", True) + """
          <span><b>Investigations</b><span>Where the work actually is</span></span></a></div>
        <div class="opitem"><a href="platform/reporting.html">""" + icon("reporting", True) + """
          <span><b>Regulatory reporting</b><span>Filed, acknowledged, explainable later</span></span></a></div>
        <div class="opitem"><a href="platform/agent-supervision.html">""" + icon("agents", True) + """
          <span><b>PSP and agent supervision</b><span>Oversight of a network, not a feature</span></span></a></div>
      </div>
    </div>
  </div>
</div></section>


<section class="band" style="padding:86px 0;color:#fff"><div class="wrap">
  <div class="rule-accent"></div>
  <h2 class="head" style="color:#fff;max-width:26ch">One customer. Eleven months
  clean, then four days.</h2>
  <p class="lead" style="color:#b7cae1;max-width:58ch">A corporate customer has traded
  since March without a single flag. Here is what happens when that changes — and what
  a supervisor can be shown about it eighteen months later. The same sequence runs for
  a retail customer, a merchant or an agent; only the scenario differs.</p>

  <div class="acts">
    <div class="act">
      <div class="when"><b>ACT ONE</b>MARCH<br>Onboarding</div>
      <div>
        <h3>Who they are, recorded in a way that still matters later</h3>
        <p>The company is resolved against the registry, ownership unwrapped past the
        holding structure, directors screened. A risk tier is set on that evidence.</p>
        <p>That tier is not a form somebody filled in. <strong style="color:#fff">It
        becomes the monitoring threshold this customer is judged against</strong> for
        as long as they bank with you.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Identity</span><b>Verified</b></div>
        <div class="k"><span>Beneficial ownership</span><b>2 individuals</b></div>
        <div class="k"><span>Screening</span><b>No match</b></div>
        <div class="k"><span>Risk tier</span><b>Standard</b></div>
        <div class="k"><span class="mono">list version recorded</span><span class="mono">OFAC 2026-03-04</span></div>
      </div>
    </div>

    <div class="act">
      <div class="when"><b>ACT TWO</b>TUESDAY<br>14:22</div>
      <div>
        <h3>The pattern breaks</h3>
        <p>Funds move out to four counterparties and return through a related account
        within the hour. Each leg sits beneath the cash reporting threshold, so nothing
        individual is remarkable.</p>
        <p>The rule that fires is not looking at transactions. It is looking at the
        shape of the round trip across accounts nobody had linked.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Scenario</span><span class="mono">ROUND_TRIP_RELATED_PARTY</span></div>
        <div class="k"><span>Legs</span><b>4</b></div>
        <div class="k"><span>Window</span><b>58 minutes</b></div>
        <div class="k"><span>Each leg</span><b>Below threshold</b></div>
        <div class="k"><span class="mono">rule version</span><span class="mono">v4.2</span></div>
      </div>
    </div>

    <div class="act">
      <div class="when"><b>ACT THREE</b>TUESDAY<br>14:23</div>
      <div>
        <h3>The money stops</h3>
        <p>The next transfer is held before it settles. Not queued for review the
        following morning — held, while somebody looks.</p>
        <p>Nobody had to be watching, and nobody had to open a second system to do it.
        <strong style="color:#fff">The fraud engine and the AML engine are looking at
        the same customer</strong>, which is the only reason this works.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Action</span><b>Hold</b></div>
        <div class="k"><span>Applied</span><b>Pre-settlement</b></div>
        <div class="k"><span>Account status</span><b>Restricted</b></div>
        <div class="k"><span class="mono">decided by</span><span class="mono">auto · policy AB-07</span></div>
      </div>
    </div>

    <div class="act">
      <div class="when"><b>ACT FOUR</b>WEDNESDAY<br>09:40</div>
      <div>
        <h3>The picture is already assembled</h3>
        <p>The analyst opens a case that already contains the March onboarding record,
        the screening history, and the three related accounts sharing a director with
        this one.</p>
        <p>They spend the morning deciding rather than assembling. That difference is
        most of what an analyst's day actually is.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Attached on open</span><b>Onboarding, screening, 2 prior alerts</b></div>
        <div class="k"><span>Linked accounts</span><b>3, shared director</b></div>
        <div class="k"><span>Prior alerts, 90 days</span><b>7</b></div>
        <div class="k"><span class="mono">maker-checker</span><span class="mono">enforced</span></div>
      </div>
    </div>

    <div class="act">
      <div class="when"><b>ACT FIVE</b>THURSDAY<br>16:05</div>
      <div>
        <h3>The report goes, and the receipt is kept</h3>
        <p>The suspicious transaction report drafts from the case that produced it — the
        transactions, the entities, the analyst's reasoning — in the format the
        regulator expects.</p>
        <p>The acknowledgement is stored against the case. <strong style="color:#fff">A
        report you cannot prove you filed is a report you did not file</strong>, as far
        as an examiner is concerned.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Filed</span><b>Thursday 16:05</b></div>
        <div class="k"><span>Trigger to filing</span><b>2 days</b></div>
        <div class="k"><span>Acknowledgement</span><b>Stored</b></div>
        <div class="k"><span class="mono">deadline applicable</span><span class="mono">within</span></div>
      </div>
    </div>

    <div class="act">
      <div class="when"><b>ACT SIX</b>EIGHTEEN MONTHS<br>LATER</div>
      <div>
        <h3>Somebody asks you to prove it</h3>
        <p>The analyst has left. The rules have changed four times. An examiner asks
        why this case was closed, and against what configuration.</p>
        <p>You can show the rule version that fired, what its threshold was set to that
        week, who approved the close and on what basis. <strong style="color:#fff">This
        is the request institutions fail most often</strong> — and it is the one every
        act above was quietly building towards.</p>
      </div>
      <div class="actpanel">
        <div class="k"><span>Rule in force</span><span class="mono">v4.2 · 2026-03 to 2026-11</span></div>
        <div class="k"><span>Threshold that week</span><b>Reconstructed</b></div>
        <div class="k"><span>Approver</span><b>Named, timestamped</b></div>
        <div class="k"><span>Evidence</span><b>Produced</b></div>
        <div class="k"><span class="mono">cited</span><span class="mono">CBN 5.5 · FATF R.11</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="sec wash"><div class="wrap">
  <p class="crumb" style="color:var(--soft);letter-spacing:.14em;font-weight:600;
  font-size:12.5px;margin:0">WHAT CHANGES FOR LEADERSHIP</p>
  <div class="lead3">
    <div>""" + icon("view") + """<h3>One connected view</h3>
      <p>Customer, transaction, alert, case and risk context in one place — so the
      answer to "what is our exposure" is a query rather than a project.</p></div>
    <div>""" + icon("governed") + """<h3>Governed decisions</h3>
      <p>Workflows, approvals, evidence and accountability connected. Every
      judgement has a name, a time and a reason attached to it.</p></div>
    <div>""" + icon("measure") + """<h3>Measurable improvement</h3>
      <p>Understand outcomes, prioritise intervention, and show what changed —
      against a recorded baseline rather than a recollection.</p></div>
  </div>
</div></section>

<section class="band" style="padding:82px 0;color:#fff"><div class="wrap">
  <div class="rule-accent"></div>
  <h2 class="head" style="color:#fff">Start where the need is greatest</h2>
  <p class="lead" style="color:#b7cae1;max-width:58ch">Nobody replaces a
  financial-crime estate in one move. <strong style="color:#fff">The platform is
  entitled per module</strong>, so you can take the one thing that is not working
  and keep everything that is.</p>
  <div class="wedge">
    <div><b>Deploy a focused wedge</b><span>One module, against the gap a diagnostic
      found. Weeks, not a programme.</span></div>
    <div><b>Demonstrate value</b><span>In production, on your own data, measured
      against where you started.</span></div>
    <div><b>Expand on the same foundation</b><span>The next module joins the same
      record. No second integration, no second reconciliation.</span></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2 class="head">Four positions we have taken</h2>

  <h3 class="sub">The work is after the alert, not at it</h3>
  <p class="body">Detection gets the demo. The investigation, the decision and the
  defence of that decision get the auditor. <strong>Investigation is three times the
  surface of the detection engine here</strong>, because that is the honest
  proportion of where an analyst's day goes.</p>

  <h3 class="sub">Fraud and money laundering are the same people</h3>
  <p class="body">They sit in different reporting lines and hear about each other
  late. The agent laundering money on Tuesday is the agent taking scam deposits on
  Thursday, and treating that as one problem requires one estate rather than two
  products.</p>

  <h3 class="sub">A number nobody can defend is not a control</h3>
  <p class="body">Somebody picked a threshold once and it has not moved since. We
  derive it — bounded by what the regulator requires you to report, limited by what
  your team can actually get through, and <strong>tested against what falls just
  underneath it</strong>. Until somebody has looked there, a threshold is a guess
  wearing a suit.</p>

  <h3 class="sub">And a vendor should not grade its own work</h3>
  <p class="body">Every platform now offers a compliance score, and almost all of them
  are marking their own homework. Ours is a separate instrument that runs against
  anybody's platform. <strong>We pointed it at our own first, and it found
  something.</strong></p>
</div></section>


<section class="sec"><div class="wrap">
  <h2 class="head">The part nobody demonstrates</h2>
  <p class="lead">Detection and cases are what a demo shows. <strong>Getting your data
  in, keeping it traceable, and holding the record together for years is more of this
  platform than the detection engine is</strong> — and it is the part that decides
  whether year three works as well as month one.</p>

  <div class="grid2">
    <div class="card"><h3>Data, and where it came from</h3>
      <p class="cap">Ingestion · connectors · lineage · quality</p>
      <ul><li>Source connectivity and certification before anything is trusted</li>
      <li>Lineage from a figure in a report back to the extract it came from</li>
      <li>Quality checks that fail loudly rather than filling gaps quietly</li>
      <li>Replay, so a period can be re-run against what it should have seen</li></ul></div>
    <div class="card"><h3>Governance and the record</h3>
      <p class="cap">Approvals · versions · audit · reconstruction</p>
      <ul><li>Rule and threshold versions retained with their parameters</li>
      <li>Approval tasks and segregation conflicts surfaced, not just logged</li>
      <li>Full audit trail, and temporal reconstruction on top of it</li>
      <li>Break-glass access that is recorded as an exception, not a login</li></ul></div>
    <div class="card"><h3>Running many institutions at once</h3>
      <p class="cap">Tenancy · isolation · onboarding</p>
      <ul><li>Isolation enforced in the database on every customer-bearing table</li>
      <li>Unset tenant means no rows, so a misconfiguration sees nothing</li>
      <li>Tenant onboarding and implementation as a managed path</li>
      <li>Incident command and continuity when something does go wrong</li></ul></div>
    <div class="card"><h3>The commercial machinery</h3>
      <p class="cap">Entitlement · metering · invoicing</p>
      <ul><li>Modules granted and withdrawn authoritatively in both directions</li>
      <li>Four metering dimensions counted separately</li>
      <li>Invoices, adjustments with approval, refunds and tax</li>
      <li>Mid-period plan changes split rather than rounded in our favour</li></ul></div>
  </div>
  <div class="quote"><p>None of this appears in a competitive feature comparison. All
  of it appears in year two.</p></div>
</div></section>

<section class="sec wash"><div class="wrap">
  <h2 class="head">Architected for what comes after the first deployment</h2>
  <p class="lead">Roughly a third of this platform never appears in a product demo:
  getting data in and keeping it traceable, running tenants without them seeing each
  other, metering what each uses, and holding the record together for years.
  <strong>Those decisions are difficult to retrofit</strong>, which is why they were
  made at the start.</p>
  <div class="designed">
    <div><p class="lab">DESIGNED FOR</p><h4>Scale without a rebuild</h4>
      <p>Multi-tenant from the first line, with isolation enforced in the database
      across every table that carries customer data — not in application code that a
      careless query can sidestep.</p></div>
    <div><p class="lab">DESIGNED FOR</p><h4>New markets as configuration</h4>
      <p>Thresholds resolve from the jurisdiction rather than being written into rules,
      and filing formats are declared per regulator. Adding a market is a configuration
      exercise, not a fork.</p></div>
    <div><p class="lab">DESIGNED FOR</p><h4>Questions asked years later</h4>
      <p>Rule versions, threshold sets and configuration parameters are retained as a
      matter of course, so a decision can be reconstructed against what was actually
      running at the time.</p></div>
    <div><p class="lab">DESIGNED FOR</p><h4>Buying one piece at a time</h4>
      <p>Modules are entitled and enforced individually, metered on volume, ingestion,
      seats and alerts as separate dimensions. The commercial model is built for a
      wedge, not only for an estate.</p></div>
    <div><p class="lab">DESIGNED FOR</p><h4>Data you can trace</h4>
      <p>Ingestion, connectors, lineage and quality are first-class rather than a
      loader script, so a figure in a report leads back to the extract it came
      from.</p></div>
    <div><p class="lab">DESIGNED FOR</p><h4>Decisions taken away from a desk</h4>
      <p>An executive projection for mobile that is deliberately not the analyst
      workspace, on devices that must be enrolled and approved before they see
      anything.</p></div>
  </div>
</div></section>
""" + nextlinks("", [
    ("What part needs to work better?", "start/diagnostic.html", "A diagnostic of your current system. No integration."),
    ("How you buy", "start/how-you-buy.html", "Per module, per usage, and stop when you want."),
    ("Independent assurance", "assurance/index.html", "Prove it to somebody who is not us."),
]), "")

    # ======================================================================
    # START HERE — the commercial path
    # ======================================================================
    page("start/index.html", "Start here",
         "Four ways to begin, and you can stop at any of them.",
         head("../", '<a href="../index.html">Home</a> · Start here',
              "You can be useful to yourself before you buy anything",
              "Most institutions we speak to are not ready to replace a platform. "
              "They are trying to close one gap and find out whether it is the one "
              "that matters.") + """
<section class="sec"><div class="wrap">
  <div class="grid2" style="margin-top:0">
    <div class="card"><h3>Run a diagnostic</h3><p class="cap">Costs you an extract</p>
      <ul><li>Send data from whatever you run today</li>
      <li>No integration, no procurement, no NDA needed</li>
      <li>A measured account of how it is actually performing</li></ul></div>
    <div class="card"><h3>Take one module</h3><p class="cap">Not the estate</p>
      <ul><li>Monitoring, screening, cases or filing, on their own</li>
      <li>Keep whatever already works</li>
      <li>Add the next when the first has earned it</li></ul></div>
  </div>
  <div class="quote"><p>Nobody buys a financial crime platform because a website was
  persuasive. They buy it because something specific is not working and somebody
  showed them what.</p></div>
</div></section>
""" + nextlinks("../", [
    ("Run a diagnostic", "start/diagnostic.html", "What it involves and what comes back."),
    ("How you buy", "start/how-you-buy.html", "Modules, metering and what you are committing to."),
    ("The platform", "platform/index.html", "What the modules actually do."),
]), "../")

    page("start/diagnostic.html", "Run a diagnostic",
         "Send an extract from whatever you run today and get a measured account of how it is performing.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Start here</a> · Diagnostic',
              "Find out what your current system is actually doing",
              "Not a demo of ours. A measured account of yours.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">What it involves</h2>
  <div class="steps">
    <div class="stp"><span class="sn">01</span><h3>You send an extract</h3><div class="sd">
      <p>Alerts, cases and outcomes from whatever platform you run today. A file, not
      an integration.</p>
      <p class="aside">No connection to your systems, no access to your production
      environment, and nothing to put through procurement.</p></div></div>
    <div class="stp"><span class="sn">02</span><h3>We tell you what it covers</h3><div class="sd">
      <p>Before any finding, a statement of what the data could and could not tell us.</p>
      <p class="aside">A diagnostic that does not say what it could not read invites a
      conclusion the data does not support. That is the failure mode we are most
      careful about.</p></div></div>
    <div class="stp"><span class="sn">03</span><h3>You get the findings</h3><div class="sd">
      <p>Where alert yield sits against institutions of similar shape. Which scenarios
      produced nothing at all. How many cases closed without a documented reason. Where
      the time from trigger to filing sits against the deadline that applies to you.</p></div></div>
    <div class="stp"><span class="sn">04</span><h3>And you decide what to do</h3><div class="sd">
      <p>Nothing obliges you to buy anything. If the answer is that your current system
      is doing its job, that is a useful thing to know and it is free to find out.</p></div></div>
  </div>

  <h3 class="sub">Then, if it is worth repeating</h3>
  <p class="body">A single diagnostic tells you where you stand. <strong>Two tell you
  whether anything you did worked</strong> — and that is the difference between a
  consulting engagement and something that keeps paying.</p>
  <div class="quote"><p>It is also the claim a professional services firm structurally
  cannot match, because they leave. An MLRO defending a tuning decision at examination
  needs evidence the change worked, and evidence is a comparison against a recorded
  baseline rather than an assertion.</p></div>
</div></section>
""" + nextlinks("../", [
    ("How you buy", "start/how-you-buy.html", "If the diagnostic finds something."),
    ("Independent assurance", "assurance/index.html", "The deeper version, for a board or an examiner."),
    ("Talk to us", "company/contact.html", "Send an extract."),
]), "../")

    page("start/how-you-buy.html", "How you buy",
         "Per module, metered per dimension, with plan changes prorated properly.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Start here</a> · How you buy',
              "Take what you need, pay for what you use",
              "We would rather have a small contract that works than a large one "
              "that stalls in procurement for a year.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">Modules, not an estate</h2>
  <p class="lead">Monitoring, screening, case management and filing are entitled
  separately. <strong>You can take one and keep whatever else already works.</strong>
  Entitlement is enforced in the platform, not tracked in a spreadsheet — a module you
  are not paying for is a module your users do not see.</p>

  <h3 class="sub">Metered on what you actually use</h3>
  <p class="body">Four dimensions, counted independently, so an institution with high
  transaction volume and few analysts is not priced like one with the opposite shape:</p>
  <div class="tbl">
    <div class="trow"><div>Transactions</div><div>Included volume, then per thousand</div></div>
    <div class="trow"><div>Ingestion</div><div>Records loaded, included then per thousand</div></div>
    <div class="trow"><div>Seats</div><div>Included users, then per additional seat</div></div>
    <div class="trow"><div>Alerts</div><div>Included alerts, then per alert</div></div>
  </div>

  <h3 class="sub">And prorated properly when you change</h3>
  <p class="body">Change plan mid-month and the period splits. <strong>Charging only
  the new plan overcharges anyone who upgraded and undercharges anyone who
  downgraded</strong>; charging both in full double-charges the month. Splitting is the
  only treatment that is right in both directions, and it is the one we implemented.</p>
  <div class="quote"><p>You should not have to audit your own invoice.</p></div>

  <h3 class="sub">What we do not do</h3>
  <p class="body">No minimum term that outlasts the value. No module you were granted
  on an upgrade and quietly kept billing for after a downgrade — entitlement is
  withdrawn as authoritatively as it is granted. And no charge for the diagnostic that
  tells you whether you need us.</p>
</div></section>
""" + nextlinks("../", [
    ("The platform", "platform/index.html", "What each module does."),
    ("Who it's for", "sectors/index.html", "Whether we are a fit for your scale."),
    ("Talk to us", "company/contact.html", "Get a quote against your volumes."),
]), "../")

    # ======================================================================
    # PLATFORM
    # ======================================================================
    page("platform/index.html", "The platform",
         "Onboarding through to filing on one customer record, with laundering and fraud handled as one estate.",
         head("../", '<a href="../index.html">Home</a> · Platform', "One record, from onboarding to filing",
              "Most institutions run verification in one system, monitoring in another and "
              "cases in a third, then spend their time reconciling the three.") + """
<section class="sec"><div class="wrap">
  <p class="lead">Here the customer record built at onboarding is the same record an
  analyst opens two years later. <strong>The risk tier set during the check drives the
  monitoring thresholds afterwards</strong>, so a decision made on day one still means
  something on day four hundred.</p>
  <div class="grid3">
    <div class="cell"><h3>Customer risk</h3><p>Identity, documents, liveness and
      ownership, resolved to a risk tier on evidence the analyst can see later.</p>
      <a href="customer-risk.html">Read more</a></div>
    <div class="cell"><h3>AML</h3><p>Laundering and fraud on the same flows,
      with thresholds resolved from the jurisdiction rather than hardcoded.</p>
      <a href="aml.html">Read more</a></div>
    <div class="cell"><h3>Investigations</h3><p>Everything the reviewer needs
      already attached, and a decision trail that survives the analyst leaving.</p>
      <a href="investigations.html">Read more</a></div>
    <div class="cell"><h3>Regulatory reporting</h3><p>Drafted from the case file,
      formatted per regulator, filed with the acknowledgement retained.</p>
      <a href="reporting.html">Read more</a></div>
    <div class="cell"><h3>PSP and agent supervision</h3><p>The specialist layer where
      laundering and fraud turn out to be the same agent.</p>
      <a href="agent-supervision.html">Read more</a></div>
    <div class="cell"><h3>Independent assurance</h3><p>Deliberately not part of the
      platform, because a system cannot credibly assess itself.</p>
      <a href="../assurance/index.html">Read more</a></div>
  </div>
  <h3 class="sub">Multi-tenant, and strict about it</h3>
  <p class="body">Isolation is enforced in the database rather than in application
  code, so a query written carelessly returns nothing rather than somebody else's
  customers. <strong>Where no tenant is set, nothing is visible</strong> — a
  misconfigured request sees an empty result instead of everything.</p>
</div></section>
""" + nextlinks("../", [
    ("AML", "platform/aml.html", "How detection is tuned and justified."),
    ("PSP and agent supervision", "platform/agent-supervision.html", "The scenarios nobody else ships."),
    ("Coverage", "coverage.html", "One platform, several regulators."),
]), "../")

    page("platform/customer-risk.html", "Customer risk",
         "Identity, documents, liveness and ownership resolved to a risk tier on evidence the analyst can see later.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · Customer risk',
              "The decision you make on day one still matters on day four hundred",
              "Most onboarding produces a yes or a no and throws away the reasoning. "
              "That reasoning is exactly what an examiner asks for later.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">What happens during the check</h2>
  <div class="steps">
    <div class="stp"><span class="sn">01</span><h3>Identity</h3><div class="sd">
      <p>Documents, biometrics and liveness, resolved against government sources where
      they are available in that market.</p></div></div>
    <div class="stp"><span class="sn">02</span><h3>The business behind it</h3><div class="sd">
      <p>For a company, resolve it against the registry and unwrap ownership past the
      holding structure to the people actually behind it.</p>
      <p class="aside">Where ownership cannot be resolved, that is recorded as a fact
      about the customer rather than quietly passed.</p></div></div>
    <div class="stp"><span class="sn">03</span><h3>Screening</h3><div class="sd">
      <p>Sanctions, PEP and watchlist checks — with the list version recorded, so a
      decision can be judged against what was actually knowable that day.</p></div></div>
    <div class="stp"><span class="sn">04</span><h3>The risk tier</h3><div class="sd">
      <p>Personal, geographic, product and behavioural factors resolve to a tier that
      drives enhanced due diligence now and monitoring thresholds afterwards.</p>
      <p class="aside">This is the part that usually gets lost. A tier that does not
      reach the monitoring engine is a form somebody filled in.</p></div></div>
  </div>
  <div class="quote"><p>Onboarding evidence is not filed away. It is the first thing
  attached to the case if that customer is ever investigated.</p></div>
</div></section>
""" + nextlinks("../", [
    ("AML", "platform/aml.html", "Where the risk tier ends up."),
    ("Investigations", "platform/investigations.html", "What the analyst sees."),
    ("Assurance", "assurance/index.html", "Testing whether the evidence exists."),
]), "../")

    page("platform/aml.html", "AML",
         "Laundering and fraud on the same flows, with thresholds derived rather than chosen.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · AML',
              "Detection you can justify, not just run",
              "Any engine will fire alerts. The question an examiner asks is why it "
              "fires where it does, and what you did about the ones it raised.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">Where did this number come from?</h2>
  <p class="lead">Somebody picked a round number once and it has not moved since. We
  work it out instead — <strong>never above what the regulator requires you to
  report</strong>, and never above what your analysts can actually get through,
  because a queue nobody clears is not a stricter control. It is a backlog with your
  name on it.</p>
  <div class="quote"><p>Then we sample what falls just underneath, to see what you are
  missing. Until somebody has done that, a threshold is a guess wearing a suit.</p></div>

  <h3 class="sub">Set the method once, not the number</h3>
  <p class="body">Thresholds are expressed as a relationship to the local regulatory
  figure rather than as an amount. Tell the system to alert beneath the cash reporting
  threshold and it resolves what that means in each market you operate in —
  <strong>from the same line of configuration</strong>.</p>

  <h3 class="sub">Laundering and fraud on the same flows</h3>
  <div class="grid2">
    <div class="card"><h3>Money laundering</h3><p class="cap">Patterns over time</p>
      <ul><li>Structuring, layering and rapid movement</li>
      <li>Dormancy and reactivation</li><li>High-risk jurisdiction exposure</li>
      <li>Velocity against the customer's own baseline</li>
      <li>Cash intensity against the declared business</li></ul></div>
    <div class="card"><h3>Fraud</h3><p class="cap">Signals in the moment</p>
      <ul><li>Device and browser fingerprint</li><li>Remote access tools and emulators</li>
      <li>Behavioural anomaly inside the session</li><li>Network and shared-attribute links</li>
      <li>Holds and interdiction before settlement</li></ul></div>
  </div>

  <h3 class="sub">And why you closed it</h3>
  <p class="body">Rule versions, threshold sets and configuration are retained. Two
  years on, when the analyst has left and the rules have changed four times, you can
  still show what the system was set to that week, what it flagged, and who signed it
  off. <strong>This is the question institutions fail most often in our
  assessments.</strong></p>
</div></section>
""" + nextlinks("../", [
    ("PSP and agent supervision", "platform/agent-supervision.html", "Scenarios built for these markets."),
    ("Investigations", "platform/investigations.html", "What happens after an alert."),
    ("Coverage", "coverage.html", "How thresholds resolve per market."),
]), "../")

    page("platform/investigations.html", "Investigations",
         "Everything the reviewer needs already attached, and a decision trail that survives the analyst leaving.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · Investigations',
              "The case opens with the context already in it",
              "An analyst who has to go and find the onboarding record, the complaint "
              "history and the linked accounts spends their day assembling rather than "
              "deciding.") + """
<section class="sec"><div class="wrap">
  <div class="grid3">
    <div class="cell"><h3>Attached on open</h3><p>Onboarding evidence, screening
      results, prior alerts, complaints and linked entities — already there.</p></div>
    <div class="cell"><h3>The entity graph</h3><p>Shared devices, addresses,
      beneficiaries and counterparties, so a single case shows the network.</p></div>
    <div class="cell"><h3>Maker-checker</h3><p>Enforced per record, so the person who
      raised it is not the person who cleared it.</p></div>
    <div class="cell"><h3>Service levels</h3><p>Ageing and queue position tracked,
      because an alert nobody reached is a finding of its own.</p></div>
    <div class="cell"><h3>Reasoning retained</h3><p>Why, in the analyst's words,
      stored beside the decision rather than in a comment field nobody exports.</p></div>
    <div class="cell"><h3>Straight to filing</h3><p>Where it escalates, the report
      drafts from the case rather than being rekeyed.</p>
      <a href="reporting.html">How filing works</a></div>
  </div>
  <div class="quote"><p>A decision trail is only worth having if somebody who was not
  there can follow it.</p></div>
</div></section>
""" + nextlinks("../", [
    ("Regulatory reporting", "platform/reporting.html", "From case to filed report."),
    ("AML", "platform/aml.html", "Where the alerts come from."),
    ("Assurance", "assurance/index.html", "Testing whether the trail holds up."),
]), "../")

    page("platform/reporting.html", "Regulatory reporting",
         "Reports drafted from the case, formatted per regulator, filed with the acknowledgement retained.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · Reporting',
              "Filed, acknowledged, and still explainable in two years",
              "Filing is where a compliance function is most visible to its regulator, "
              "and where rekeying causes the most damage.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">Drafted from the case, not from scratch</h2>
  <p class="lead">The suspicious transaction report assembles from the case file that
  produced it — the transactions, the entities, the analyst's reasoning and the
  evidence — in the format that regulator expects.</p>

  <div class="tbl">
    <div class="trow"><div>Nigeria</div><div>Filed to the NFIU through goAML
      <span class="ref">CBN AML/CFT/CPF · in production</span></div></div>
    <div class="trow"><div>Ghana</div><div>Financial Intelligence Centre
      <span class="ref">AML Act 1044</span></div></div>
    <div class="trow"><div>Kenya</div><div>Financial Reporting Centre
      <span class="ref">POCAMLA s.44 · s.44(6)</span></div></div>
    <div class="trow"><div>South Africa</div><div>Financial Intelligence Centre
      <span class="ref">FIC Act s.29 · s.28</span></div></div>
    <div class="trow"><div>United Kingdom</div><div>National Crime Agency
      <span class="ref">POCA 2002 · MLR 2017</span></div></div>
  </div>

  <h3 class="sub">The acknowledgement is part of the record</h3>
  <p class="body">A report you cannot prove you filed is a report you did not file, as
  far as an examiner is concerned. <strong>Acknowledgements are stored against the
  case</strong>, with the timestamp, so the question "when did you tell us" has an
  answer that is not somebody's recollection.</p>

  <h3 class="sub">Timeliness is assessed separately</h3>
  <p class="body">Late filing is a breach in itself, distinct from whether the report
  was correct. The platform tracks the gap between the trigger and the filing, because
  that is the number a supervisor will compute if you do not.</p>
</div></section>
""" + nextlinks("../", [
    ("Coverage", "coverage.html", "Which regulators and what binds you."),
    ("Investigations", "platform/investigations.html", "Where the report comes from."),
    ("Assurance", "assurance/how-it-works.html", "How filing is tested."),
]), "../")

    page("platform/agent-supervision.html", "PSP and agent supervision",
         "Scenarios built for agent networks and wallets, where laundering and fraud turn out to be the same agent.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · PSP and agent supervision',
              "The agent laundering money on Tuesday takes scam deposits on Thursday",
              "A platform designed for correspondent banking has never seen either, "
              "and cannot treat them as one problem if it sells AML and fraud "
              "separately.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">What a generic engine misses</h2>
  <div class="grid2">
    <div class="card"><h3>Same-agent round trip</h3><p class="cap">SAME_AGENT_ROUND_TRIP</p>
      <ul><li>Funds leave and return through one agent inside a short window</li>
      <li>Each leg beneath the reporting threshold</li>
      <li>Invisible to any rule looking at single transactions</li></ul></div>
    <div class="card"><h3>Cross-agent structuring</h3><p class="cap">CROSS_AGENT_GEO_STRUCTURING</p>
      <ul><li>Structuring spread across agents and locations</li>
      <li>No single agent trips a threshold</li>
      <li>Only visible when the network is treated as one</li></ul></div>
    <div class="card"><h3>Complaint clustering</h3><p class="cap">AGENT_COMPLAINT_SPIKE</p>
      <ul><li>Cash-not-credited complaints concentrating on one agent</li>
      <li>Frequently the first signal an agent has gone bad</li>
      <li>Lives in the complaints system at most institutions, unread</li></ul></div>
    <div class="card"><h3>Wallet behaviour</h3><p class="cap">DORMANT_WALLET_REACTIVATION · NIGHT_TIME_VELOCITY</p>
      <ul><li>Long-dormant wallets moving quickly on reactivation</li>
      <li>Activity outside the customer's established pattern</li>
      <li>Velocity before a behavioural baseline exists</li></ul></div>
  </div>

  <h3 class="sub">Thresholds that fit the network</h3>
  <p class="body">Agent volumes differ by an order of magnitude between a city network
  and a rural cooperative. <strong>A micro-structuring rule tuned for one alerts on
  every ordinary customer of the other</strong>, so thresholds are configured per
  tenant rather than shipped as constants.</p>

  <div class="quote"><p>An agent suspended for laundering and an agent held for scam
  exposure are the same agent.</p></div>
</div></section>
""" + nextlinks("../", [
    ("Payment service banks", "sectors/payment-service-banks.html", "Who this was built for."),
    ("AML", "platform/aml.html", "How the thresholds are set."),
    ("Request a demo", "company/contact.html", "See it with your own network."),
]), "../")


    page("platform/fraud.html", "Fraud",
         "Interdiction before the money leaves, on the same record as the AML estate.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Platform</a> · Fraud',
              "Stop it before the money goes",
              "Money laundering is a pattern you find afterwards. Fraud is a decision "
              "you have seconds to make, and the two share a customer.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">Signals in the moment, not patterns over weeks</h2>
  <div class="grid2" style="margin-top:0">
    <div class="card"><h3>What the session tells you</h3><p class="cap">Before the transfer</p>
      <ul><li>Device and browser fingerprint</li>
      <li>Remote access tools and emulators</li>
      <li>Behaviour that does not match the account holder</li>
      <li>Velocity against this customer's own baseline</li></ul></div>
    <div class="card"><h3>What you can do about it</h3><p class="cap">While it still matters</p>
      <ul><li>Hold the payment before it settles</li>
      <li>Block an agent or a device automatically</li>
      <li>Reach the customer before they send it</li>
      <li>Open a case with the session evidence attached</li></ul></div>
  </div>

  <h3 class="sub">Scam intervention</h3>
  <p class="body">A customer being socially engineered is not committing fraud, they are
  losing money to it. <strong>Reaching them before the transfer completes is a
  different capability from scoring the transaction</strong>, and most AML platforms
  do not have it because it was never their problem.</p>

  <h3 class="sub">Including your own people</h3>
  <p class="body">Insider events and network links are tracked on the same graph as
  customer relationships. An employee sharing attributes with a customer account is a
  pattern worth surfacing, and it does not appear in either system alone.</p>

  <h3 class="sub">And scoring you can explain</h3>
  <p class="body">Model scores are versioned. When somebody asks why a payment was
  held in March, the answer is which model, at what version, scoring what — not a
  number with no provenance.</p>

  <div class="quote"><p>The agent laundering money on Tuesday is the agent taking scam
  deposits on Thursday. Two vendors cannot see that.</p></div>
</div></section>
""" + nextlinks("../", [
    ("AML", "platform/aml.html", "The other half of the same estate."),
    ("PSP and agent supervision", "platform/agent-supervision.html", "Where the two meet."),
    ("Investigations", "platform/investigations.html", "What happens after either fires."),
]), "../")

    # ======================================================================
    # ASSURANCE
    # ======================================================================
    page("assurance/index.html", "Independent assurance",
         "A separate system that tests whether your controls can actually be evidenced.",
         head("../", '<a href="../index.html">Home</a> · Assurance',
              "Every vendor offers a compliance score. Almost all of them mark their own homework.",
              "A score your software gives itself is worth very little to the person "
              "signing the attestation.") + """
<section class="sec"><div class="wrap">
  <p class="lead">So the assessment is a separate system, with no shared identifiers
  with the platform. It asks your team the questions a supervisor would and records
  what actually comes back. <strong>It runs against institutions on any platform,
  including ours</strong> — we pointed it at our own first, and it found something.</p>

  <h3 class="sub">Two halves, and the second tests the first</h3>
  <div class="grid2">
    <div class="card"><h3>The control assessment</h3><p class="cap">What you have</p>
      <ul><li>Every control scored on whether evidence exists</li>
      <li>Whether it is adequate, current and governed</li>
      <li>And whether it is proportionate to your size</li>
      <li>Cited to the instruments that bind you locally</li></ul></div>
    <div class="card"><h3>The evidence exercise</h3><p class="cap">What you can produce</p>
      <ul><li>Supervisory information requests, issued in writing</li>
      <li>Answered by your team, unaided</li>
      <li>Recorded by source — system of record, spreadsheet, or recollection</li>
      <li>And by what it cost in hours</li></ul></div>
  </div>

  <div class="quote"><p>Where a control is assessed as in place and the request testing
  it cannot be answered, the report says so — and names the obligations you cannot
  currently evidence.</p></div>

  <p class="body">That finding is what no questionnaire reaches. A supervisor treats a
  control that cannot be evidenced as a control that is not there, and most
  institutions do not discover which of theirs fall into that category until somebody
  external asks.</p>

  <h3 class="sub">It is an engagement, not a form</h3>
  <p class="body"><strong>It takes your senior compliance people's time.</strong> That
  is the point of it — an examination you fail in a meeting room costs nothing, and the
  same one in front of a regulator costs a great deal. We would rather be honest about
  the commitment than have you discover it in week two.</p>
</div></section>
""" + nextlinks("../", [
    ("How an assessment runs", "assurance/how-it-works.html", "What actually happens, week by week."),
    ("What you receive", "assurance/deliverables.html", "The documents and who they are for."),
    ("The platform", "platform/index.html", "What the assessment is separate from."),
]), "../")

    page("assurance/how-it-works.html", "How an assessment runs",
         "What actually happens during a control assurance engagement, and what it asks of your team.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Assurance</a> · How it runs',
              "What actually happens",
              "Stated plainly, including the parts that cost you time.") + """
<section class="sec"><div class="wrap">
  <div class="steps">
    <div class="stp"><span class="sn">01</span><h3>Scope and period</h3><div class="sd">
      <p>We agree which legal entity is being assessed, in which jurisdiction, and over
      what period. The period is then locked.</p>
      <p class="aside">Without a recorded period, no reader can tell which obligations
      applied or whether the evidence was current.</p></div></div>
    <div class="stp"><span class="sn">02</span><h3>The evidence request</h3><div class="sd">
      <p>You receive the full list of what will be asked for, ahead of the session. No
      surprises — the exercise is not a trap, it is a rehearsal.</p></div></div>
    <div class="stp"><span class="sn">03</span><h3>The control assessment</h3><div class="sd">
      <p>Working through each control with the people who operate it, recording what
      exists, how mature it is, and whether the evidence was actually produced.</p>
      <p class="aside">Assessed against what an institution your size is expected to
      hold, not against a tier one bank's budget.</p></div></div>
    <div class="stp"><span class="sn">04</span><h3>The evidence exercise</h3><div class="sd">
      <p>Supervisory information requests issued in writing and answered by your team
      without our help. We record what came back, from where, and how long it took.</p>
      <p class="aside">This is the part that costs real time. It is also the only part
      that tells you what an examination would actually find.</p></div></div>
    <div class="stp"><span class="sn">05</span><h3>Findings and report</h3><div class="sd">
      <p>Controls rated well whose evidence could not be produced are named, with the
      obligations they put at risk. Strengths are recorded too.</p></div></div>
    <div class="stp"><span class="sn">06</span><h3>Re-measurement</h3><div class="sd">
      <p>The assessment becomes a baseline. Next year measures against it, so progress
      is a number rather than an assertion.</p></div></div>
  </div>

  <h3 class="sub">What we do not claim</h3>
  <p class="body">This measures readiness, not compliance. <strong>A strong result is
  not evidence of compliance with any obligation.</strong> It records what you could
  produce; it does not verify that what you produced was correct. Where a control was
  not assessed, nothing is recorded — absence of a finding is not evidence of
  capability.</p>
  <p class="body">And where our reading of a local rule has not been through a lawyer in
  that country, the report says so on the front page.</p>
</div></section>
""" + nextlinks("../", [
    ("What you receive", "assurance/deliverables.html", "The documents and their audiences."),
    ("Coverage", "coverage.html", "Which regulators we cite."),
    ("Talk to us", "company/contact.html", "Discuss scope for your institution."),
]), "../")

    page("assurance/deliverables.html", "What you receive",
         "The documents produced by an assessment, and who each is written for.",
         head("../", '<a href="../index.html">Home</a> · <a href="index.html">Assurance</a> · What you receive',
              "Four documents, four audiences",
              "A single report written for everybody gets read properly by nobody.") + """
<section class="sec"><div class="wrap">
  <div class="grid2">
    <div class="card"><h3>Board pack</h3><p class="cap">For the audit committee</p>
      <ul><li>Opens with the decisions required, not the findings</li>
      <li>What you are being asked to accept, and what it would cost to close</li>
      <li>Owner and date columns left blank, deliberately</li>
      <li>Short enough to be read before the meeting</li></ul></div>
    <div class="card"><h3>Assurance report</h3><p class="cap">For the MLRO and internal audit</p>
      <ul><li>Every control, every dimension, with the evidence recorded</li>
      <li>Controls assessed as in place that could not be evidenced</li>
      <li>Obligations cited to the instruments in force locally</li>
      <li>Scope and limitations stated on the face of it</li></ul></div>
    <div class="card"><h3>Progress report</h3><p class="cap">For whoever owns remediation</p>
      <ul><li>Movement against the recorded baseline</li>
      <li>What improved, and what regressed</li>
      <li>Whether the trajectory reaches the target</li>
      <li>Blunt about it when it does not</li></ul></div>
    <div class="card"><h3>Submission pack</h3><p class="cap">Where a regulator expects one</p>
      <ul><li>In the structure that regulator asks for</li>
      <li>Assembled from the same assessed record</li>
      <li>Currently Nigeria; other markets receive the neutral report</li></ul></div>
  </div>

  <h3 class="sub">A note on the group case</h3>
  <p class="body">Where an institution holds several regulated entities, the assessment
  produces a group view and an entity comparison — and <strong>deliberately does not
  produce a group score</strong>. A figure assembled from entities that define a
  measure differently is arithmetically valid and analytically meaningless.</p>
  <div class="quote"><p>Better to report per entity with no total than a total nobody
  can defend.</p></div>
</div></section>
""" + nextlinks("../", [
    ("How an assessment runs", "assurance/how-it-works.html", "The engagement, step by step."),
    ("Who it's for", "sectors/payment-service-banks.html", "Proportionality by institution size."),
    ("Talk to us", "company/contact.html", "Scope an assessment."),
]), "../")

    # ======================================================================
    # SECTORS
    # ======================================================================
    # The nav points here, so it needs a landing page rather than dropping
    # somebody straight into one sector they may not be.
    page("sectors/index.html", "Who it's for",
         "Which institutions the platform serves today, and where we would tell you we are not the right fit.",
         head("../", '<a href="../index.html">Home</a> · Who it\'s for',
              "We would rather tell you now than three months into a procurement",
              "The platform is configured per jurisdiction rather than per institution "
              "type, so the question is the scale you operate at, not the category you "
              "sit in.") + """
<section class="sec"><div class="wrap">
  <div class="grid3" style="margin-top:0">
    <div class="cell"><h3>Payment service banks and wallets</h3><p>What the platform was
      built around, and what is running in production today.</p>
      <a href="payment-service-banks.html">Read more</a></div>
    <div class="cell"><h3>Microfinance and small OFIs</h3><p>Held to your own standard,
      not to one written for a bank fifty times your size.</p>
      <a href="microfinance.html">Read more</a></div>
    <div class="cell"><h3>Commercial banks</h3><p>The full estate, with the evidence
      discipline an examiner expects.</p>
      <a href="commercial-banks.html">Read more</a></div>
    <div class="cell"><h3>Development finance</h3><p>Few transactions, large amounts,
      donor money — where velocity rules are the wrong shape.</p>
      <a href="development-finance.html">Read more</a></div>
  </div>

  <h3 class="sub">And where we would say no</h3>
  <p class="body">If your volumes sit beyond what we have demonstrated, or your risk
  profile needs something we have not built, we will say so on the first call.
  <strong>We keep the list of what we have not yet shown</strong>, and we will read
  it to you before you ask.</p>
</div></section>
""" + nextlinks("../", [
    ("The platform", "platform/index.html", "What you would be running."),
    ("Independent assurance", "assurance/index.html", "Finding out what you can evidence."),
    ("Talk to us", "company/contact.html", "A demo with your own rules."),
]), "../")

    sectors = [
        ("payment-service-banks", "Payment service banks and wallets",
         "Where the platform was built, and what is running in production today.",
         "This is what we built for first",
         "Agent networks and mobile wallets carry the volume in these markets, and the "
         "typologies that come with them are not in a system designed for correspondent banking.",
         [("Agent-specific detection", "Round trips, cross-agent structuring, complaint clustering and suspension — treated as one problem across laundering and fraud."),
          ("Thresholds that fit your network", "A city network and a rural cooperative differ by an order of magnitude. Configured per tenant, not shipped as a constant."),
          ("Real-time holds", "Stop the transfer while somebody looks, rather than reading about it the next morning."),
          ("In production", "Running today, filing to the regulator, with the audit trail to show for it.")]),
        ("microfinance", "Microfinance banks and small OFIs",
         "Held to your own standard, not to one written for a bank fifty times your size.",
         "A careful manual process is the right answer here",
         "Most compliance assessments apply one absolute standard and hand a small "
         "institution a list of things it was never meant to buy.",
         [("Proportionate assessment", "Controls judged against what an institution your size is expected to hold. A documented, consistently applied arrangement is a pass, not a finding."),
          ("No crisis manufactured", "A well-run small institution should be told it is well run."),
          ("Room to grow into", "The same platform serves larger institutions, so growing does not mean replacing."),
          ("Honest about cost", "We will tell you if an assessment is more than you need right now.")]),
        ("commercial-banks", "Commercial banks",
         "The full estate, with the evidence discipline an examiner expects.",
         "Everything the function does, and the proof it worked",
         "Tier 2 and tier 3 institutions get the same platform as everybody else — "
         "configured per jurisdiction rather than per institution type.",
         [("Converged AML and fraud", "One estate rather than two products and two reporting lines that hear about each other late."),
          ("Decision reconstruction", "Two years on, show what the rules were set to that week and who approved the close."),
          ("Multi-market", "Several regulators, one platform, one picture for the board."),
          ("Straight about scale", "Tell us your volumes and we will tell you honestly whether we are ready for them.")]),
        ("development-finance", "Development finance",
         "Few transactions, large amounts, donor money — where velocity rules are the wrong shape.",
         "Where the funds came from matters more than how fast they moved",
         "A monitoring estate tuned for transaction velocity is built for the wrong "
         "risk. We would rather say so than pretend otherwise.",
         [("Source of funds", "Provenance, beneficiary verification and use-of-proceeds carry the weight, not transaction pace."),
          ("Counterparty depth", "Ownership unwrapped past the holding structure, with unresolved ownership recorded as a fact rather than passed."),
          ("Donor and mandate reporting", "Obligations to funders alongside obligations to regulators."),
          ("Proportionate", "Low volume does not mean low scrutiny, and the assessment reflects that.")]),
    ]
    for slug, title, desc, h1, lede, points in sectors:
        cells = "".join(f'<div class="cell"><h3>{t}</h3><p>{d}</p></div>' for t, d in points)
        page(f"sectors/{slug}.html", title, desc,
             head("../", f'<a href="../index.html">Home</a> · Who it\'s for · {title}', h1, lede) + f"""
<section class="sec"><div class="wrap">
  <div class="grid3" style="margin-top:0">{cells}</div>
  <h3 class="sub">Would we be straight with you?</h3>
  <p class="body">We would rather tell you now than three months into a procurement.
  If your volumes or your risk profile sit outside what we can demonstrate today, we
  will say so on the first call. <strong>The list of what we have not yet shown is
  shorter than the list of what we have, and we keep both.</strong></p>
</div></section>
""" + nextlinks("../", [
    ("The platform", "platform/index.html", "What you would be running."),
    ("Independent assurance", "assurance/index.html", "Finding out what you can evidence."),
    ("Talk to us", "company/contact.html", "A demo with your own rules."),
]), "../")

    # ======================================================================
    # COVERAGE
    # ======================================================================
    page("coverage.html", "Coverage",
         "The markets supported, the regulators, and how thresholds resolve per jurisdiction.",
         head("", '<a href="index.html">Home</a> · Coverage',
              "Open a new market on a Monday",
              "Set the method once and the system works out what it means locally.") + """
<section class="sec"><div class="wrap">
  <p class="lead">Tell it to alert beneath the local cash reporting threshold and it
  resolves the figure for each market you operate in. <strong>Your team learns one
  platform and your board sees one picture.</strong></p>

  <div class="tbl">
    <div class="trow"><div>Nigeria</div><div>Central Bank of Nigeria, filing to the NFIU
      <span class="ref">CBN AML/CFT/CPF · in production</span></div></div>
    <div class="trow"><div>Ghana</div><div>Bank of Ghana and the Financial Intelligence Centre
      <span class="ref">AML Act 1044 · BoG/FIC Guideline</span></div></div>
    <div class="trow"><div>Kenya</div><div>Financial Reporting Centre and the Central Bank
      <span class="ref">POCAMLA s.44 · s.44(6)</span></div></div>
    <div class="trow"><div>South Africa</div><div>Financial Intelligence Centre
      <span class="ref">FIC Act s.42 · s.29 · Guidance Note 7B</span></div></div>
    <div class="trow"><div>United Kingdom</div><div>Financial Conduct Authority
      <span class="ref">MLR 2017 · SYSC 6.3</span></div></div>
    <div class="trow"><div>And the standard</div><div>Cited as what domestic law is
      assessed against, never as law itself
      <span class="ref">FATF 40 Recommendations</span></div></div>
  </div>

  <h3 class="sub">What binds, and what informs</h3>
  <p class="body">A statute binds. A guidance note is what a supervisor examines
  against. A draft directive is neither, yet. <strong>The reports distinguish
  them</strong>, because presenting an international standard beside domestic law as
  though both were binding is the kind of error that costs credibility in a meeting.</p>

  <h3 class="sub">Where a market is not yet researched</h3>
  <p class="body">You get the international baseline, clearly labelled as such, with
  the regulator and regional body named. That is thinner and it is honest — better
  than a pack that looks local and is not.</p>

  <h3 class="sub">And what has not been through a lawyer</h3>
  <p class="body">Our reading of a local rule is research, not legal advice. Where a
  jurisdiction has not been reviewed by a qualified practitioner in that country, the
  report says so on the front page. <strong>You should know which parts to take to
  counsel.</strong></p>
</div></section>
""" + nextlinks("", [
    ("Regulatory reporting", "platform/reporting.html", "Filing per regulator."),
    ("AML", "platform/aml.html", "How thresholds resolve."),
    ("Assurance", "assurance/index.html", "Assessed against local obligations."),
]), "")

    # ======================================================================
    # COMPANY
    # ======================================================================
    page("company/about.html", "About",
         "Who we are, what we have built, and what we have not.",
         head("../", '<a href="../index.html">Home</a> · Company · About',
              "Built by people who have run this function",
              "INFERIVA exists because the systems sold into these markets were "
              "designed for somewhere else, and assessed by instruments that accept "
              "description in place of evidence.") + """
<section class="sec"><div class="wrap">
  <h2 class="head">What we build</h2>
  <p class="lead">A financial crime operations platform — onboarding, screening,
  monitoring, cases and filing — with money laundering and fraud handled as one estate
  and a specialist layer where agent networks and wallets carry the volume.</p>
  <p class="lead">And a separate assurance instrument, because <strong>a platform
  assessing its own controls is a self-assessment however good its data.</strong></p>

  <h3 class="sub">What we are honest about</h3>
  <p class="body">We are early. We have a production tenant, a platform that files to
  a regulator, and an assessment instrument we have run against our own systems and
  found things with.</p>
  <p class="body">We do not yet have SOC 2 Type II, we have not demonstrated screening
  at the volume a systemic institution requires, and our obligation mappings have not
  been through qualified counsel in every market. <strong>We keep that list and we
  will show it to you</strong> — it is shorter than the one on the other side, and a
  vendor who cannot tell you what they have not done is a vendor who has not
  checked.</p>

  <div class="quote"><p>An examination you fail in private costs nothing. That applies
  to us as much as to anybody we assess.</p></div>

  <h3 class="sub">Where we work</h3>
  <p class="body">Lagos and London, serving institutions across West Africa, East
  Africa, Southern Africa and the United Kingdom. The platform is configured per
  jurisdiction rather than rebuilt per market, so where we go next is a question of
  demand rather than engineering.</p>
</div></section>
""" + nextlinks("../", [
    ("The platform", "platform/index.html", "What we have built."),
    ("Coverage", "coverage.html", "Where it runs."),
    ("Contact", "company/contact.html", "Talk to us."),
]), "../")

    page("company/contact.html", "Contact",
         "Request a demonstration configured for your markets, or discuss a control assessment.",
         head("../", '<a href="../index.html">Home</a> · Company · Contact',
              "Tell us what you run and where",
              "We will show you the platform set up the way it would work for you, "
              "rather than a generic walkthrough.") + """
<section class="sec tight"><div class="wrap">
  <div class="grid3" style="margin-top:0">
    <div class="cell"><h3>A demonstration</h3><p>Configured for your jurisdictions, your
      products and the thresholds that bind you. Usually an hour.</p></div>
    <div class="cell"><h3>A control assessment</h3><p>A proper engagement. We will scope
      it honestly, including what it will cost your team in time.</p></div>
    <div class="cell"><h3>Or a straight answer</h3><p>If we are not the right fit for
      your volumes or your risk profile, we would rather say so on the first call.</p></div>
  </div>
</div></section>
""" + nextlinks("../", [
    ("The platform", "platform/index.html", "What you would be seeing."),
    ("Assurance", "assurance/how-it-works.html", "What an assessment involves."),
    ("About", "company/about.html", "Who you would be working with."),
]), "../")
