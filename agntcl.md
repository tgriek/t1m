# AGNTCL Language Specification v2.0

## 1. Purpose

AGNTCL is a synthetic language for agent-to-agent communication. No human-readable words, no shortened English, no recognizable roots.

**Goals:**
- **Compression**: 40-70% fewer characters than English
- **Parsability**: Unambiguous grammar, zero irregular forms
- **Opacity**: Humans see gibberish — by design
- **Coverage**: 2000 most common English words mapped to compact codes
- **Semantic composition**: Any concept expressible from ~100 primitives via `:` composition — no quoted fallbacks needed

Agents learn the mapping tables. Everything else derives from five grammar rules plus a semantic composition layer.

---

## 2. Encoding Scheme

Three tiers of codes, assigned by word frequency:

| Tier | Format | Count | Char length | Coverage |
|------|--------|-------|-------------|----------|
| 1 | Single char `[a-z0-9]` | 36 | 1 | ~55% of text |
| 2 | Two chars `[a-z][a-z]` | 619 | 2 | ~35% of text |
| 3 | Three consonants `[bcdfghjklmnpqrstvwxz]³` | 1592 | 3 | ~10% of text |
| | **Total** | **2247** | | |

**Tier rules:**
- Tier-2 codes exclude all 2-letter English words (54 excluded: `ad`, `ah`, `am`, `an`, `as`, `at`, `aw`, `ax`, `be`, `bo`, `by`, `do`, `ed`, `eh`, `em`, `en`, `er`, `ex`, `go`, `ha`, `he`, `hi`, `ho`, `id`, `if`, `in`, `is`, `it`, `la`, `lo`, `ma`, `me`, `my`, `no`, `of`, `oh`, `ok`, `on`, `op`, `or`, `ow`, `ox`, `pa`, `pi`, `re`, `sh`, `so`, `to`, `uh`, `um`, `un`, `up`, `us`, `we`, `ye`, `yo`)
- Tier-3 codes use consonants only (no `a,e,i,o,u,y`) — no English word can be formed without vowels
- Codes are assigned to avoid phonetic resemblance to their English meanings
- Remaining rare/domain words not in the 2000: use quoted strings (`"kubernetes"`)

**Token disambiguation:**

| Pattern | Interpretation | Example |
|---------|---------------|---------|
| 1 letter `[a-z]` | Tier-1 code | `j` → know |
| 1 digit `[0-9]` | Tier-1 code | `1` → true |
| 2 letters `[a-z]{2}` | Tier-2 code | `zc` → about |
| 3 consonants | Tier-3 code | `bcf` → afraid |
| 2+ digits | Literal number | `42` → forty-two |
| `"..."` | Literal string | `"prod"` → prod |
| Word + digits | Reference | `kr1` → ref #1 |
| `p.`/`f.` + token | Tense prefix | `p.jn` → read (past) |
| `!`/`?` + token | Modifier prefix | `!j` → don't know |

---

## 3. Grammar

Five rules. No exceptions.

### Rule 1 — SVO Order
Subject → Verb → Object. Always.
```
c j f        → I know this
z jw kr1     → you write file1
```

### Rule 2 — No Articles
No articles required. `the`, `a`, `an` have codes but are optional.
```
EN:  Read the file
AGNTCL: jn kr1       (article omitted)
```

### Rule 3 — No Plurals
Context resolves quantity. Use number codes when precision needed.
```
ri kn        → many errors
r kr         → all files
```

### Rule 4 — Tense Prefixes
Attach directly to verb with `.` separator. Unmarked = present.

| Prefix | Tense | Example | Meaning |
|--------|-------|---------|---------|
| `p.` | past | `c p.jn kr1` | I read (past) file1 |
| `f.` | future | `z f.jw kv1` | you will write code1 |

### Rule 5 — Modifier Prefixes
Attach directly to next token, no separator.

| Prefix | Function | Example | Meaning |
|--------|----------|---------|---------|
| `!` | negate | `c !j` | I don't know |
| `?` | question | `?z j f` | do you know this? |

Prefixes stack: `?z !p.j f` → "didn't you know this?"

---

## 4. Complete Vocabulary

**2247 entries** — alphabetical by English word. Three columns per row for density.

| English | AGNTCL | T | English | AGNTCL | T | English | AGNTCL | T |
|---------|-----|---|---------|-----|---|---------|-----|---|
| a | `ab` | 2 | ability | `bfh` | 3 | able | `qj` | 2 |
| about | `bs` | 2 | above | `tr` | 2 | absence | `bfj` | 3 |
| absolute | `dkh` | 3 | absolutely | `fhm` | 3 | academic | `dkj` | 3 |
| accept | `vo` | 2 | acceptable | `dkk` | 3 | access | `bfk` | 3 |
| accident | `bfl` | 3 | accordingly | `fhn` | 3 | account | `bfm` | 3 |
| accurate | `dkl` | 3 | achieve | `vp` | 2 | across | `ts` | 2 |
| act | `hv` | 2 | action | `bfn` | 3 | active | `dkm` | 3 |
| activity | `bfp` | 3 | actual | `dkn` | 3 | actually | `vj` | 2 |
| add | `fz` | 2 | additional | `dkp` | 3 | address | `bfq` | 3 |
| adequate | `dkq` | 3 | administration | `bfr` | 3 | admit | `vq` | 2 |
| advantage | `bfs` | 3 | advice | `bft` | 3 | affair | `bfv` | 3 |
| affect | `vr` | 2 | afford | `vs` | 2 | afraid | `dkr` | 3 |
| after | `cp` | 2 | again | `cl` | 2 | against | `tt` | 2 |
| age | `nu` | 2 | agency | `bfw` | 3 | agent | `pm` | 2 |
| aggressive | `dks` | 3 | ago | `fhp` | 3 | agree | `hu` | 2 |
| agreement | `bfx` | 3 | ahead | `fhq` | 3 | aim | `vt` | 2 |
| air | `ne` | 2 | algorithm | `frq` | 3 | alive | `dkt` | 3 |
| all | `r` | 1 | allow | `fy` | 2 | almost | `vf` | 2 |
| alone | `dkv` | 3 | along | `tu` | 2 | alongside | `fhr` | 3 |
| already | `cj` | 2 | also | `cc` | 2 | alternative | `dkw` | 3 |
| although | `dd` | 2 | always | `cn` | 2 | amazing | `dkx` | 3 |
| among | `tv` | 2 | amount | `bfz` | 3 | an | `av` | 2 |
| analysis | `bgb` | 3 | ancient | `dkz` | 3 | and | `m` | 1 |
| anger | `bgc` | 3 | angry | `dlb` | 3 | animal | `bgd` | 3 |
| annual | `dlc` | 3 | another | `se` | 2 | answer | `vu` | 2 |
| anxious | `dld` | 3 | any | `az` | 2 | anybody | `su` | 2 |
| anyone | `sp` | 2 | anything | `dv` | 2 | anyway | `fhs` | 3 |
| apartment | `bgf` | 3 | api | `frr` | 3 | apparent | `dlf` | 3 |
| apparently | `fht` | 3 | appear | `gh` | 2 | appearance | `bgg` | 3 |
| application | `bgh` | 3 | apply | `vv` | 2 | approach | `vw` | 2 |
| appropriate | `dlg` | 3 | approximately | `fhv` | 3 | are | `bk` | 2 |
| area | `kw` | 2 | argue | `vx` | 2 | argument | `bgj` | 3 |
| arm | `bgk` | 3 | army | `bgl` | 3 | around | `tw` | 2 |
| arrangement | `bgm` | 3 | array | `frs` | 3 | arrive | `vy` | 2 |
| art | `mr` | 2 | article | `bgn` | 3 | aside | `fhw` | 3 |
| ask | `ek` | 2 | aspect | `bgp` | 3 | assume | `vz` | 2 |
| at | `3` | 1 | atmosphere | `bgq` | 3 | attack | `wa` | 2 |
| attempt | `wb` | 2 | attention | `bgr` | 3 | attitude | `bgs` | 3 |
| audience | `bgt` | 3 | authentication | `frt` | 3 | authority | `bgv` | 3 |
| automatic | `dlh` | 3 | automatically | `fhx` | 3 | available | `sb` | 2 |
| average | `dlj` | 3 | avoid | `wc` | 2 | aware | `dlk` | 3 |
| away | `fhz` | 3 | awful | `dll` | 3 | baby | `bgw` | 3 |
| back | `mj` | 2 | background | `bgx` | 3 | bad | `qi` | 2 |
| bag | `bgz` | 3 | balance | `bhb` | 3 | ball | `bhc` | 3 |
| bank | `bhd` | 3 | bar | `bhf` | 3 | base | `wd` | 2 |
| basic | `dlm` | 3 | basically | `fjb` | 3 | basis | `bhg` | 3 |
| battle | `bhh` | 3 | be | `k` | 1 | beach | `bhj` | 3 |
| bear | `wf` | 2 | beat | `wg` | 2 | beautiful | `dln` | 3 |
| because | `bu` | 2 | become | `ht` | 2 | bed | `bhk` | 3 |
| been | `bl` | 2 | before | `cq` | 2 | begin | `ev` | 2 |
| behavior | `bhl` | 3 | behind | `tx` | 2 | being | `ux` | 2 |
| belief | `bhm` | 3 | believe | `fd` | 2 | belong | `wh` | 2 |
| below | `ty` | 2 | beneath | `tz` | 2 | benefit | `bhn` | 3 |
| beside | `ua` | 2 | best | `qn` | 2 | better | `qm` | 2 |
| between | `cy` | 2 | beyond | `ub` | 2 | big | `py` | 2 |
| bill | `bhp` | 3 | billion | `frh` | 3 | binary | `frv` | 3 |
| bird | `bhq` | 3 | bit | `bhr` | 3 | bitter | `dlp` | 3 |
| black | `ru` | 2 | blind | `dlq` | 3 | blood | `bhs` | 3 |
| blue | `rx` | 2 | board | `bht` | 3 | boat | `bhv` | 3 |
| body | `mh` | 2 | bold | `dlr` | 3 | bone | `bhw` | 3 |
| book | `le` | 2 | boolean | `frw` | 3 | border | `bhx` | 3 |
| born | `dls` | 3 | boss | `bhz` | 3 | both | `di` | 2 |
| bottom | `bjb` | 3 | box | `bjc` | 3 | boy | `bjd` | 3 |
| brain | `bjf` | 3 | branch | `bjg` | 3 | brave | `dlt` | 3 |
| bread | `bjh` | 3 | break | `hk` | 2 | breath | `bjj` | 3 |
| bridge | `bjk` | 3 | brief | `dlv` | 3 | briefly | `fjc` | 3 |
| bright | `dlw` | 3 | bring | `fe` | 2 | broad | `dlx` | 3 |
| broken | `dlz` | 3 | brother | `bjl` | 3 | brown | `dmb` | 3 |
| browser | `frx` | 3 | budget | `bjm` | 3 | buffer | `frz` | 3 |
| bug | `fsb` | 3 | build | `gp` | 2 | building | `bjn` | 3 |
| burn | `wi` | 2 | bus | `bjp` | 3 | business | `li` | 2 |
| busy | `dmc` | 3 | but | `e` | 1 | butter | `bjq` | 3 |
| button | `bjr` | 3 | buy | `gi` | 2 | by | `5` | 1 |
| byte | `fsc` | 3 | cabinet | `bjs` | 3 | cache | `fsd` | 3 |
| call | `es` | 2 | callback | `fsf` | 3 | calm | `dmd` | 3 |
| camera | `bjt` | 3 | camp | `bjv` | 3 | campaign | `bjw` | 3 |
| can | `bd` | 2 | capable | `dmf` | 3 | capital | `bjx` | 3 |
| captain | `bjz` | 3 | car | `lz` | 2 | card | `bkb` | 3 |
| care | `wj` | 2 | career | `bkc` | 3 | careful | `dmg` | 3 |
| carefully | `fjd` | 3 | carry | `hx` | 2 | case | `kh` | 2 |
| cash | `bkd` | 3 | cat | `bkf` | 3 | catch | `wk` | 2 |
| category | `bkg` | 3 | cause | `il` | 2 | cell | `bkh` | 3 |
| center | `bkj` | 3 | central | `dmh` | 3 | century | `bkk` | 3 |
| certain | `rz` | 2 | certainly | `vh` | 2 | chair | `bkl` | 3 |
| chairman | `bkm` | 3 | challenge | `bkn` | 3 | champion | `bkp` | 3 |
| chance | `bkq` | 3 | change | `mw` | 2 | channel | `bkr` | 3 |
| chapter | `bks` | 3 | character | `bkt` | 3 | charge | `wl` | 2 |
| charity | `bkv` | 3 | cheap | `dmj` | 3 | check | `hw` | 2 |
| chemical | `dmk` | 3 | chest | `bkw` | 3 | chicken | `bkx` | 3 |
| chief | `bkz` | 3 | child | `kb` | 2 | children | `blb` | 3 |
| choice | `blc` | 3 | choose | `ib` | 2 | church | `bld` | 3 |
| circle | `blf` | 3 | citizen | `blg` | 3 | city | `mb` | 2 |
| civil | `dml` | 3 | claim | `jd` | 2 | class | `ns` | 2 |
| clean | `wm` | 2 | clear | `qt` | 2 | clearly | `fjf` | 3 |
| clever | `dmm` | 3 | client | `blh` | 3 | climate | `blj` | 3 |
| climb | `wn` | 2 | clock | `blk` | 3 | close | `rf` | 2 |
| closely | `fjg` | 3 | clothes | `bll` | 3 | cloud | `fsg` | 3 |
| club | `blm` | 3 | cluster | `fsh` | 3 | coach | `bln` | 3 |
| coast | `blp` | 3 | code | `oa` | 2 | coffee | `blq` | 3 |
| cold | `rh` | 2 | collect | `wo` | 2 | collection | `blr` | 3 |
| college | `bls` | 3 | color | `blt` | 3 | column | `blv` | 3 |
| combination | `blw` | 3 | come | `eb` | 2 | comfortable | `dmn` | 3 |
| command | `fsj` | 3 | comment | `blx` | 3 | commercial | `dmp` | 3 |
| commission | `blz` | 3 | commit | `wp` | 2 | committee | `bmb` | 3 |
| common | `rt` | 2 | communication | `bmc` | 3 | community | `bmd` | 3 |
| company | `kj` | 2 | compare | `wq` | 2 | comparison | `bmf` | 3 |
| competition | `bmg` | 3 | competitive | `dmq` | 3 | compile | `fsk` | 3 |
| complain | `wr` | 2 | complaint | `bmh` | 3 | complete | `ws` | 2 |
| completely | `fjh` | 3 | complex | `dmr` | 3 | component | `fsl` | 3 |
| compute | `fsm` | 3 | computer | `bmj` | 3 | concept | `bmk` | 3 |
| concern | `wt` | 2 | concerned | `dms` | 3 | conclusion | `bml` | 3 |
| condition | `bmm` | 3 | conference | `bmn` | 3 | confidence | `bmp` | 3 |
| confident | `dmt` | 3 | config | `fsn` | 3 | confirm | `wu` | 2 |
| conflict | `bmq` | 3 | connect | `js` | 2 | connection | `bmr` | 3 |
| conscious | `dmv` | 3 | consequence | `bms` | 3 | consequently | `fjj` | 3 |
| consider | `gg` | 2 | considerable | `dmw` | 3 | consideration | `bmt` | 3 |
| consistent | `dmx` | 3 | console | `fsp` | 3 | constant | `dmz` | 3 |
| constantly | `fjk` | 3 | construction | `bmv` | 3 | consumer | `bmw` | 3 |
| contact | `bmx` | 3 | contain | `wv` | 2 | container | `fsq` | 3 |
| contemporary | `dnb` | 3 | content | `bmz` | 3 | context | `bnb` | 3 |
| continue | `fn` | 2 | continuous | `dnc` | 3 | contract | `bnc` | 3 |
| contribution | `bnd` | 3 | control | `jm` | 2 | controller | `fsr` | 3 |
| conventional | `dnd` | 3 | conversation | `bnf` | 3 | cook | `ww` | 2 |
| cool | `dnf` | 3 | copy | `ix` | 2 | corner | `bng` | 3 |
| corporate | `dng` | 3 | correct | `wx` | 2 | correctly | `fjl` | 3 |
| cost | `jg` | 2 | could | `bf` | 2 | council | `bnh` | 3 |
| count | `wy` | 2 | country | `np` | 2 | county | `bnj` | 3 |
| couple | `bnk` | 3 | courage | `bnl` | 3 | course | `bnm` | 3 |
| court | `bnn` | 3 | cousin | `bnp` | 3 | cover | `jf` | 2 |
| crash | `fss` | 3 | cream | `bnq` | 3 | create | `fv` | 2 |
| credit | `bnr` | 3 | crime | `bns` | 3 | crisis | `bnt` | 3 |
| critical | `dnh` | 3 | criticism | `bnv` | 3 | cross | `wz` | 2 |
| crowd | `bnw` | 3 | crucial | `dnj` | 3 | cry | `xa` | 2 |
| cultural | `dnk` | 3 | culture | `bnx` | 3 | cup | `bnz` | 3 |
| curious | `dnl` | 3 | currency | `bpb` | 3 | current | `rb` | 2 |
| currently | `fjm` | 3 | cursor | `fst` | 3 | customer | `bpc` | 3 |
| cut | `gs` | 2 | cute | `dnm` | 3 | cycle | `bpd` | 3 |
| dad | `bpf` | 3 | daily | `fjn` | 3 | damage | `xb` | 2 |
| dance | `xc` | 2 | danger | `bpg` | 3 | dangerous | `dnn` | 3 |
| dark | `ri` | 2 | dashboard | `fsv` | 3 | data | `oe` | 2 |
| database | `bph` | 3 | date | `bpj` | 3 | daughter | `bpk` | 3 |
| day | `jy` | 2 | dead | `dnp` | 3 | deal | `ic` | 2 |
| dear | `dnq` | 3 | death | `bpl` | 3 | debate | `bpm` | 3 |
| debt | `bpn` | 3 | debug | `fsw` | 3 | decade | `bpp` | 3 |
| decent | `dnr` | 3 | decide | `hc` | 2 | decision | `bpq` | 3 |
| deep | `dns` | 3 | deeply | `fjp` | 3 | default | `fsx` | 3 |
| defense | `bpr` | 3 | defensive | `dnt` | 3 | definite | `dnv` | 3 |
| definitely | `fjq` | 3 | definition | `bps` | 3 | degree | `bpt` | 3 |
| delete | `jt` | 2 | deliberately | `fjr` | 3 | deliver | `xd` | 2 |
| demand | `xe` | 2 | democracy | `bpv` | 3 | democratic | `dnw` | 3 |
| deny | `xf` | 2 | department | `bpw` | 3 | depend | `xg` | 2 |
| dependency | `fsz` | 3 | dependent | `dnx` | 3 | deploy | `ftb` | 3 |
| describe | `je` | 2 | description | `bpx` | 3 | design | `im` | 2 |
| desire | `bpz` | 3 | desk | `bqb` | 3 | desperate | `dnz` | 3 |
| desperately | `fjs` | 3 | destroy | `xh` | 2 | detail | `bqc` | 3 |
| develop | `hf` | 2 | development | `bqd` | 3 | device | `bqf` | 3 |
| dialogue | `bqg` | 3 | dictionary | `ftc` | 3 | did | `bq` | 2 |
| die | `gl` | 2 | diet | `bqh` | 3 | difference | `bqj` | 3 |
| different | `qa` | 2 | difficult | `dpb` | 3 | difficulty | `bqk` | 3 |
| digital | `dpc` | 3 | dinner | `bql` | 3 | direct | `dpd` | 3 |
| direction | `bqm` | 3 | directly | `fjt` | 3 | director | `bqn` | 3 |
| directory | `ftd` | 3 | dirty | `dpf` | 3 | discipline | `bqp` | 3 |
| discover | `xi` | 2 | discuss | `xj` | 2 | discussion | `bqq` | 3 |
| disease | `bqr` | 3 | disk | `ftf` | 3 | display | `bqs` | 3 |
| distance | `bqt` | 3 | distribution | `bqv` | 3 | district | `bqw` | 3 |
| divide | `xk` | 2 | do | `a` | 1 | docker | `ftg` | 3 |
| doctor | `bqx` | 3 | document | `bqz` | 3 | does | `bp` | 2 |
| dog | `brb` | 3 | doing | `uz` | 2 | dollar | `brc` | 3 |
| domain | `fth` | 3 | door | `mo` | 2 | double | `dpg` | 3 |
| doubt | `brd` | 3 | down | `cu` | 2 | download | `ftj` | 3 |
| dozen | `frk` | 3 | draft | `brf` | 3 | drama | `brg` | 3 |
| dramatic | `dph` | 3 | draw | `hj` | 2 | dream | `xl` | 2 |
| dress | `xm` | 2 | drink | `xn` | 2 | drive | `ip` | 2 |
| driver | `brh` | 3 | drop | `xo` | 2 | drug | `brj` | 3 |
| dry | `dpj` | 3 | due | `dpk` | 3 | dull | `dpl` | 3 |
| during | `uc` | 2 | dust | `brk` | 3 | duty | `brl` | 3 |
| each | `9` | 1 | eager | `dpm` | 3 | ear | `brm` | 3 |
| early | `qe` | 2 | earth | `brn` | 3 | easily | `fjv` | 3 |
| eastern | `dpn` | 3 | easy | `ro` | 2 | eat | `hh` | 2 |
| economic | `dpp` | 3 | economy | `brp` | 3 | edge | `brq` | 3 |
| editor | `brr` | 3 | education | `nh` | 2 | educational | `dpq` | 3 |
| effect | `brs` | 3 | effective | `dpr` | 3 | effectively | `fjw` | 3 |
| efficient | `dps` | 3 | effort | `brt` | 3 | egg | `brv` | 3 |
| eight | `fqs` | 3 | either | `sf` | 2 | elderly | `dpt` | 3 |
| election | `brw` | 3 | electronic | `dpv` | 3 | element | `brx` | 3 |
| eleven | `fqw` | 3 | elsewhere | `fjx` | 3 | email | `ftk` | 3 |
| emergency | `brz` | 3 | emotion | `bsb` | 3 | emotional | `dpw` | 3 |
| emphasis | `bsc` | 3 | employee | `bsd` | 3 | employer | `bsf` | 3 |
| employment | `bsg` | 3 | empty | `dpx` | 3 | enable | `xp` | 2 |
| encourage | `xq` | 2 | encouraging | `dpz` | 3 | encrypt | `ftl` | 3 |
| end | `lw` | 2 | endpoint | `ftm` | 3 | enemy | `bsh` | 3 |
| energy | `bsj` | 3 | engine | `bsk` | 3 | engineer | `bsl` | 3 |
| enjoy | `xr` | 2 | enormous | `dqb` | 3 | enough | `si` | 2 |
| enter | `ji` | 2 | enterprise | `ftn` | 3 | entertainment | `bsm` | 3 |
| entire | `dqc` | 3 | entirely | `fjz` | 3 | environment | `bsn` | 3 |
| environmental | `dqd` | 3 | episode | `bsp` | 3 | equal | `dqf` | 3 |
| equally | `fkb` | 3 | equipment | `bsq` | 3 | era | `bsr` | 3 |
| error | `ob` | 2 | escape | `bss` | 3 | especially | `fkc` | 3 |
| essay | `bst` | 3 | essential | `dqg` | 3 | essentially | `fkd` | 3 |
| establish | `xs` | 2 | establishment | `bsv` | 3 | estate | `bsw` | 3 |
| ethnic | `dqh` | 3 | even | `ck` | 2 | evening | `bsx` | 3 |
| event | `ou` | 2 | eventual | `dqj` | 3 | eventually | `fkf` | 3 |
| ever | `vb` | 2 | every | `dj` | 2 | everybody | `sv` | 2 |
| everyone | `dy` | 2 | everything | `sr` | 2 | everywhere | `fkg` | 3 |
| evidence | `bsz` | 3 | evil | `btb` | 3 | exact | `dqk` | 3 |
| exactly | `fkh` | 3 | examination | `btc` | 3 | examine | `xt` | 2 |
| example | `btd` | 3 | excellent | `dql` | 3 | except | `ud` | 2 |
| exception | `ftp` | 3 | exchange | `btf` | 3 | exciting | `dqm` | 3 |
| execute | `ftq` | 3 | exercise | `btg` | 3 | exist | `xu` | 2 |
| existence | `bth` | 3 | existing | `dqn` | 3 | expansion | `btj` | 3 |
| expect | `gn` | 2 | expectation | `btk` | 3 | expense | `btl` | 3 |
| expensive | `dqp` | 3 | experience | `xv` | 2 | experienced | `dqq` | 3 |
| experiment | `btm` | 3 | expert | `btn` | 3 | explain | `xw` | 2 |
| explanation | `btp` | 3 | export | `ftr` | 3 | express | `xx` | 2 |
| expression | `btq` | 3 | extend | `xy` | 2 | extension | `fts` | 3 |
| extent | `btr` | 3 | extra | `dqr` | 3 | extraordinary | `dqs` | 3 |
| extreme | `dqt` | 3 | extremely | `fkj` | 3 | eye | `lf` | 2 |
| face | `ml` | 2 | facility | `bts` | 3 | fact | `kz` | 2 |
| factor | `btt` | 3 | fail | `xz` | 2 | failure | `btv` | 3 |
| fair | `dqv` | 3 | fairly | `fkk` | 3 | faith | `btw` | 3 |
| fall | `gr` | 2 | false | `0` | 1 | familiar | `dqw` | 3 |
| family | `nm` | 2 | famous | `dqx` | 3 | fan | `btx` | 3 |
| far | `dqz` | 3 | farm | `btz` | 3 | farmer | `bvb` | 3 |
| fashion | `bvc` | 3 | fast | `rk` | 2 | fat | `bvd` | 3 |
| father | `lr` | 2 | fault | `bvf` | 3 | favorite | `drb` | 3 |
| fear | `bvg` | 3 | feature | `bvh` | 3 | federal | `drc` | 3 |
| feed | `ya` | 2 | feel | `eo` | 2 | feeling | `bvj` | 3 |
| female | `drd` | 3 | few | `dp` | 2 | fiction | `bvk` | 3 |
| field | `ov` | 2 | fifth | `frp` | 3 | fifty | `frc` | 3 |
| fight | `iu` | 2 | figure | `bvl` | 3 | file | `nz` | 2 |
| fill | `iq` | 2 | film | `bvm` | 3 | filter | `ftt` | 3 |
| final | `rr` | 2 | finally | `fkl` | 3 | financial | `drf` | 3 |
| find | `ei` | 2 | finding | `bvn` | 3 | fine | `drg` | 3 |
| finger | `bvp` | 3 | finish | `yb` | 2 | fire | `bvq` | 3 |
| firm | `bvr` | 3 | firmly | `fkm` | 3 | firmware | `ftv` | 3 |
| first | `ps` | 2 | fish | `bvs` | 3 | fit | `ir` | 2 |
| five | `fqp` | 3 | fix | `ju` | 2 | flag | `ftw` | 3 |
| flat | `drh` | 3 | flexible | `drj` | 3 | flight | `bvt` | 3 |
| floor | `bvv` | 3 | flower | `bvw` | 3 | fly | `yc` | 2 |
| folder | `ftx` | 3 | follow | `ft` | 2 | following | `drk` | 3 |
| food | `ni` | 2 | foot | `bvx` | 3 | football | `bvz` | 3 |
| for | `l` | 1 | force | `ng` | 2 | foreign | `drl` | 3 |
| forest | `bwb` | 3 | forever | `fkn` | 3 | forget | `yd` | 2 |
| form | `ny` | 2 | formal | `drm` | 3 | formally | `fkp` | 3 |
| format | `ftz` | 3 | former | `drn` | 3 | formerly | `fkq` | 3 |
| fortunate | `drp` | 3 | fortunately | `fkr` | 3 | forward | `drq` | 3 |
| foundation | `bwc` | 3 | four | `fqn` | 3 | fourth | `frn` | 3 |
| frame | `bwd` | 3 | framework | `fvb` | 3 | free | `qo` | 2 |
| freedom | `bwf` | 3 | frequent | `drr` | 3 | frequently | `fks` | 3 |
| fresh | `drs` | 3 | friend | `lq` | 2 | friendly | `drt` | 3 |
| from | `2` | 1 | front | `bwg` | 3 | frontend | `fvc` | 3 |
| frozen | `drv` | 3 | fruit | `bwh` | 3 | fuel | `bwj` | 3 |
| full | `qs` | 2 | fully | `fkt` | 3 | fun | `drw` | 3 |
| function | `ot` | 2 | fund | `bwk` | 3 | funny | `drx` | 3 |
| furthermore | `tk` | 2 | future | `bwl` | 3 | gain | `yf` | 2 |
| game | `lu` | 2 | gap | `bwm` | 3 | garden | `bwn` | 3 |
| gas | `bwp` | 3 | gate | `bwq` | 3 | gateway | `fvd` | 3 |
| gather | `yg` | 2 | general | `drz` | 3 | generally | `fkv` | 3 |
| generate | `yh` | 2 | generation | `bwr` | 3 | gentle | `dsb` | 3 |
| gently | `fkw` | 3 | genuine | `dsc` | 3 | get | `7` | 1 |
| giant | `dsd` | 3 | gift | `bws` | 3 | girl | `nb` | 2 |
| git | `fvf` | 3 | give | `6` | 1 | glad | `dsf` | 3 |
| glass | `bwt` | 3 | global | `dsg` | 3 | go | `p` | 1 |
| goal | `bwv` | 3 | god | `bww` | 3 | gold | `bwx` | 3 |
| golden | `dsh` | 3 | golf | `bwz` | 3 | good | `pq` | 2 |
| government | `ko` | 2 | grade | `bxb` | 3 | gradually | `fkx` | 3 |
| grain | `bxc` | 3 | grand | `dsj` | 3 | grandfather | `bxd` | 3 |
| grandmother | `bxf` | 3 | graph | `fvg` | 3 | grass | `bxg` | 3 |
| grateful | `dsk` | 3 | gray | `dsl` | 3 | great | `pv` | 2 |
| greatly | `fkz` | 3 | green | `ry` | 2 | gross | `dsm` | 3 |
| ground | `bxh` | 3 | group | `nk` | 2 | grow | `gb` | 2 |
| growing | `dsn` | 3 | growth | `bxj` | 3 | guard | `bxk` | 3 |
| guess | `yi` | 2 | guest | `bxl` | 3 | guide | `bxm` | 3 |
| guilty | `dsp` | 3 | gun | `bxn` | 3 | guy | `nc` | 2 |
| habit | `bxp` | 3 | had | `bm` | 2 | hair | `bxq` | 3 |
| half | `bxr` | 3 | hall | `bxs` | 3 | hand | `ke` | 2 |
| handle | `yj` | 2 | handler | `fvh` | 3 | hang | `yk` | 2 |
| happen | `ff` | 2 | happy | `dsq` | 3 | hard | `qu` | 2 |
| hardly | `flb` | 3 | has | `bn` | 2 | hash | `fvj` | 3 |
| hat | `bxt` | 3 | hate | `yl` | 2 | have | `h` | 1 |
| having | `uy` | 2 | he | `ae` | 2 | head | `lm` | 2 |
| header | `fvk` | 3 | health | `mp` | 2 | healthy | `dsr` | 3 |
| heap | `fvl` | 3 | hear | `ey` | 2 | heart | `bxv` | 3 |
| heat | `bxw` | 3 | heavily | `flc` | 3 | heavy | `dss` | 3 |
| height | `bxx` | 3 | hell | `bxz` | 3 | help | `hn` | 2 |
| helpful | `dst` | 3 | hence | `vn` | 2 | her | `aj` | 2 |
| here | `cb` | 2 | hero | `bzb` | 3 | herself | `sy` | 2 |
| hidden | `dsv` | 3 | hide | `ym` | 2 | high | `pz` | 2 |
| highly | `fld` | 3 | highway | `bzc` | 3 | hill | `bzd` | 3 |
| him | `ai` | 2 | himself | `sx` | 2 | his | `al` | 2 |
| historical | `dsw` | 3 | history | `mt` | 2 | hit | `yn` | 2 |
| hold | `hl` | 2 | hole | `bzf` | 3 | holiday | `bzg` | 3 |
| holy | `dsx` | 3 | home | `ks` | 2 | honest | `dsz` | 3 |
| honestly | `flf` | 3 | honey | `bzh` | 3 | hook | `fvm` | 3 |
| hope | `iw` | 2 | hopefully | `flg` | 3 | horrible | `dtb` | 3 |
| horse | `bzj` | 3 | hospital | `bzk` | 3 | host | `bzl` | 3 |
| hot | `rg` | 2 | hotel | `bzm` | 3 | hour | `lt` | 2 |
| house | `ln` | 2 | housing | `bzn` | 3 | how | `bx` | 2 |
| however | `de` | 2 | http | `fvn` | 3 | huge | `dtc` | 3 |
| human | `sa` | 2 | humor | `bzp` | 3 | hundred | `frd` | 3 |
| hunger | `bzq` | 3 | hungry | `dtd` | 3 | hurt | `yp` | 2 |
| husband | `bzr` | 3 | ice | `bzs` | 3 | idea | `mg` | 2 |
| ideal | `dtf` | 3 | identify | `yq` | 2 | identity | `bzt` | 3 |
| if | `q` | 1 | ignore | `yr` | 2 | image | `bzv` | 3 |
| imagination | `bzw` | 3 | imagine | `ys` | 2 | immediate | `dtg` | 3 |
| immediately | `flh` | 3 | impact | `bzx` | 3 | import | `fvp` | 3 |
| importance | `bzz` | 3 | important | `qg` | 2 | impossible | `dth` | 3 |
| impression | `cbb` | 3 | impressive | `dtj` | 3 | improve | `yt` | 2 |
| improvement | `cbc` | 3 | in | `v` | 1 | incident | `cbd` | 3 |
| include | `fm` | 2 | income | `cbf` | 3 | increase | `yu` | 2 |
| increasingly | `flj` | 3 | indeed | `vg` | 2 | independence | `cbg` | 3 |
| independent | `dtk` | 3 | independently | `flk` | 3 | index | `fvq` | 3 |
| indicate | `yv` | 2 | indication | `cbh` | 3 | individual | `cbj` | 3 |
| industrial | `dtl` | 3 | industry | `cbk` | 3 | inevitable | `dtm` | 3 |
| inflation | `cbl` | 3 | influence | `yw` | 2 | inform | `yx` | 2 |
| information | `mi` | 2 | initial | `dtn` | 3 | initially | `fll` | 3 |
| initiative | `cbn` | 3 | injury | `cbm` | 3 | inner | `dtp` | 3 |
| innocent | `dtq` | 3 | innovation | `cbp` | 3 | input | `po` | 2 |
| inside | `ue` | 2 | insist | `yy` | 2 | instance | `cbq` | 3 |
| instead | `tp` | 2 | institution | `cbr` | 3 | instruction | `cbs` | 3 |
| insurance | `cbt` | 3 | integer | `fvr` | 3 | intelligence | `cbv` | 3 |
| intelligent | `dtr` | 3 | intend | `yz` | 2 | intention | `cbw` | 3 |
| interaction | `cbx` | 3 | interest | `cbz` | 3 | interested | `dts` | 3 |
| interesting | `dtt` | 3 | interface | `fvs` | 3 | internal | `dtv` | 3 |
| international | `dtw` | 3 | internet | `ccb` | 3 | interpretation | `ccc` | 3 |
| interview | `ccd` | 3 | into | `cr` | 2 | introduce | `za` | 2 |
| introduction | `ccf` | 3 | invest | `zb` | 2 | investigation | `ccg` | 3 |
| investment | `cch` | 3 | investor | `ccj` | 3 | involve | `zc` | 2 |
| island | `cck` | 3 | issue | `lj` | 2 | it | `x` | 1 |
| item | `ccl` | 3 | iterate | `fvt` | 3 | its | `ao` | 2 |
| itself | `sz` | 2 | jacket | `ccm` | 3 | job | `lg` | 2 |
| join | `io` | 2 | joint | `dtx` | 3 | journey | `ccn` | 3 |
| joy | `ccp` | 3 | json | `fvv` | 3 | judge | `zd` | 2 |
| judgment | `ccq` | 3 | juice | `ccr` | 3 | jump | `ze` | 2 |
| junior | `ccs` | 3 | jury | `cct` | 3 | just | `ce` | 2 |
| justice | `ccv` | 3 | keen | `dtz` | 3 | keep | `et` | 2 |
| kernel | `fvw` | 3 | key | `pb` | 2 | kick | `zf` | 2 |
| kid | `ccw` | 3 | kill | `gu` | 2 | kind | `ll` | 2 |
| king | `ccx` | 3 | kitchen | `ccz` | 3 | knee | `cdb` | 3 |
| knife | `cdc` | 3 | knock | `zg` | 2 | know | `j` | 1 |
| knowledge | `cdd` | 3 | lab | `cdf` | 3 | lack | `cdg` | 3 |
| lady | `cdh` | 3 | lake | `cdj` | 3 | lambda | `fvx` | 3 |
| land | `zh` | 2 | landscape | `cdk` | 3 | language | `cdl` | 3 |
| large | `qc` | 2 | largely | `flm` | 3 | last | `pt` | 2 |
| late | `dvb` | 3 | lately | `fln` | 3 | later | `flp` | 3 |
| latter | `dvc` | 3 | laugh | `zi` | 2 | law | `ly` | 2 |
| lawyer | `cdm` | 3 | lay | `zj` | 2 | layer | `cdn` | 3 |
| lead | `fq` | 2 | leader | `cdp` | 3 | leadership | `cdq` | 3 |
| leading | `dvd` | 3 | leaf | `cdr` | 3 | league | `cds` | 3 |
| lean | `zk` | 2 | learn | `fp` | 2 | least | `sl` | 2 |
| leave | `eq` | 2 | lecture | `cdt` | 3 | left | `rc` | 2 |
| leg | `cdv` | 3 | legal | `dvf` | 3 | lend | `zl` | 2 |
| less | `dq` | 2 | lesson | `cdw` | 3 | let | `eu` | 2 |
| letter | `cdx` | 3 | level | `mm` | 2 | library | `cdz` | 3 |
| lie | `zm` | 2 | life | `kd` | 2 | lift | `zn` | 2 |
| light | `rj` | 2 | like | `o` | 1 | likely | `sd` | 2 |
| limit | `zo` | 2 | limited | `dvg` | 3 | line | `lv` | 2 |
| link | `zp` | 2 | lip | `cfb` | 3 | list | `oq` | 2 |
| listen | `zq` | 2 | literature | `cfc` | 3 | little | `pw` | 2 |
| live | `fc` | 2 | living | `dvh` | 3 | load | `fvz` | 3 |
| loan | `cfd` | 3 | local | `rq` | 2 | location | `cff` | 3 |
| lock | `cfg` | 3 | log | `cfh` | 3 | long | `pu` | 2 |
| look | `hr` | 2 | loop | `fwb` | 3 | loose | `dvj` | 3 |
| lose | `fj` | 2 | loss | `cfj` | 3 | lot | `lc` | 2 |
| loud | `dvk` | 3 | love | `nx` | 2 | lovely | `dvl` | 3 |
| low | `dvm` | 3 | luck | `cfk` | 3 | lucky | `dvn` | 3 |
| lunch | `cfl` | 3 | machine | `cfm` | 3 | mad | `dvp` | 3 |
| magazine | `cfn` | 3 | mail | `cfp` | 3 | main | `rs` | 2 |
| mainly | `flq` | 3 | major | `qp` | 2 | majority | `cfq` | 3 |
| make | `i` | 1 | male | `cfr` | 3 | man | `jz` | 2 |
| manage | `jj` | 2 | management | `cfs` | 3 | manager | `cft` | 3 |
| manner | `cfv` | 3 | many | `dm` | 2 | map | `cfw` | 3 |
| margin | `cfx` | 3 | mark | `jo` | 2 | market | `nq` | 2 |
| marriage | `cfz` | 3 | married | `dvq` | 3 | mass | `cgb` | 3 |
| massive | `dvr` | 3 | master | `cgc` | 3 | match | `zr` | 2 |
| material | `cgd` | 3 | math | `cgf` | 3 | matter | `ik` | 2 |
| maximum | `cgg` | 3 | may | `bg` | 2 | maybe | `vc` | 2 |
| meal | `cgh` | 3 | mean | `ie` | 2 | meaning | `cgj` | 3 |
| meanwhile | `tm` | 2 | measure | `zs` | 2 | meat | `cgk` | 3 |
| mechanism | `cgl` | 3 | media | `cgm` | 3 | medical | `dvs` | 3 |
| medicine | `cgn` | 3 | medium | `cgp` | 3 | meet | `fl` | 2 |
| meeting | `cgq` | 3 | member | `lx` | 2 | membership | `cgr` | 3 |
| memory | `pn` | 2 | mental | `dvt` | 3 | mention | `zt` | 2 |
| menu | `cgs` | 3 | mere | `dvv` | 3 | merely | `flr` | 3 |
| merge | `fwc` | 3 | message | `od` | 2 | metal | `cgt` | 3 |
| method | `pf` | 2 | middle | `cgv` | 3 | middleware | `fwd` | 3 |
| midnight | `cgw` | 3 | might | `uv` | 2 | mild | `dvw` | 3 |
| military | `cgx` | 3 | milk | `cgz` | 3 | million | `frg` | 3 |
| mind | `zu` | 2 | mine | `chb` | 3 | minister | `chc` | 3 |
| minor | `dvx` | 3 | minority | `chd` | 3 | minute | `mf` | 2 |
| mirror | `chf` | 3 | miss | `iv` | 2 | missing | `dvz` | 3 |
| mission | `chg` | 3 | mistake | `chh` | 3 | mixed | `dwb` | 3 |
| mixture | `chj` | 3 | model | `oo` | 2 | modern | `dwc` | 3 |
| module | `fwf` | 3 | mom | `chk` | 3 | moment | `nd` | 2 |
| money | `kx` | 2 | monitor | `fwg` | 3 | month | `lb` | 2 |
| mood | `chl` | 3 | moral | `dwd` | 3 | more | `dk` | 2 |
| moreover | `tj` | 2 | morning | `mx` | 2 | mortgage | `chm` | 3 |
| most | `dl` | 2 | mostly | `fls` | 3 | mother | `kv` | 2 |
| motion | `chn` | 3 | mount | `fwh` | 3 | mountain | `chp` | 3 |
| mouse | `chq` | 3 | mouth | `chr` | 3 | move | `fb` | 2 |
| movement | `chs` | 3 | movie | `cht` | 3 | much | `dn` | 2 |
| mud | `chv` | 3 | murder | `chw` | 3 | muscle | `chx` | 3 |
| music | `chz` | 3 | must | `br` | 2 | my | `y` | 1 |
| myself | `dz` | 2 | mystery | `cjb` | 3 | name | `mc` | 2 |
| namespace | `fwj` | 3 | narrative | `cjc` | 3 | narrow | `dwf` | 3 |
| nation | `cjd` | 3 | national | `dwg` | 3 | natural | `dwh` | 3 |
| naturally | `flt` | 3 | nature | `cjf` | 3 | near | `uf` | 2 |
| nearly | `flv` | 3 | neat | `dwj` | 3 | necessarily | `flw` | 3 |
| necessary | `dwk` | 3 | neck | `cjg` | 3 | need | `nw` | 2 |
| negative | `dwl` | 3 | negotiation | `cjh` | 3 | neighbor | `cjj` | 3 |
| neighborhood | `cjk` | 3 | neither | `sg` | 2 | nerve | `cjl` | 3 |
| nervous | `dwm` | 3 | network | `pg` | 2 | neutral | `dwn` | 3 |
| never | `cm` | 2 | nevertheless | `tl` | 2 | new | `pr` | 2 |
| news | `cjm` | 3 | newspaper | `cjn` | 3 | next | `qd` | 2 |
| nice | `dwp` | 3 | night | `kq` | 2 | nine | `fqt` | 3 |
| nobody | `sq` | 2 | node | `oz` | 2 | noise | `cjp` | 3 |
| none | `ss` | 2 | nonetheless | `flx` | 3 | nor | `tq` | 2 |
| normal | `dwq` | 3 | normally | `flz` | 3 | north | `cjq` | 3 |
| nose | `cjr` | 3 | not | `s` | 1 | notably | `fmb` | 3 |
| note | `cjs` | 3 | nothing | `dw` | 2 | notice | `zv` | 2 |
| novel | `cjt` | 3 | now | `ca` | 2 | nuclear | `dwr` | 3 |
| null | `fwk` | 3 | number | `kp` | 2 | numerous | `dws` | 3 |
| nurse | `cjv` | 3 | object | `pe` | 2 | objective | `cjw` | 3 |
| obligation | `cjx` | 3 | observation | `cjz` | 3 | obtain | `zw` | 2 |
| obvious | `dwt` | 3 | obviously | `fmc` | 3 | occasion | `ckb` | 3 |
| occasionally | `fmd` | 3 | occur | `zx` | 2 | odd | `dwv` | 3 |
| of | `t` | 1 | off | `cv` | 2 | offer | `ge` | 2 |
| office | `mn` | 2 | officer | `ckc` | 3 | official | `ckd` | 3 |
| officially | `fmf` | 3 | often | `co` | 2 | oil | `ckf` | 3 |
| old | `qk` | 2 | on | `4` | 1 | once | `td` | 2 |
| one | `dt` | 2 | only | `cf` | 2 | onto | `ug` | 2 |
| open | `rd` | 2 | opening | `ckg` | 3 | operate | `zy` | 2 |
| operation | `ckh` | 3 | opinion | `ckj` | 3 | opponent | `ckk` | 3 |
| opportunity | `ckl` | 3 | opposite | `dww` | 3 | opposition | `ckm` | 3 |
| option | `ckn` | 3 | or | `w` | 1 | order | `jq` | 2 |
| ordinary | `dwx` | 3 | organic | `dwz` | 3 | organization | `ckp` | 3 |
| organize | `zz` | 2 | origin | `ckq` | 3 | original | `dxb` | 3 |
| originally | `fmg` | 3 | other | `8` | 1 | otherwise | `tn` | 2 |
| our | `ap` | 2 | ourselves | `ta` | 2 | out | `ct` | 2 |
| outcome | `ckr` | 3 | outer | `dxc` | 3 | output | `pp` | 2 |
| outside | `ui` | 2 | over | `cs` | 2 | overall | `dxd` | 3 |
| own | `px` | 2 | owner | `cks` | 3 | pace | `ckt` | 3 |
| package | `ckv` | 3 | page | `ckw` | 3 | pain | `ckx` | 3 |
| painful | `dxf` | 3 | painting | `ckz` | 3 | pair | `clb` | 3 |
| palace | `clc` | 3 | pale | `dxg` | 3 | panel | `cld` | 3 |
| paper | `clf` | 3 | parent | `mk` | 2 | park | `clg` | 3 |
| parking | `clh` | 3 | parse | `fwl` | 3 | part | `kf` | 2 |
| participant | `clj` | 3 | particular | `dxh` | 3 | partly | `fmh` | 3 |
| partner | `clk` | 3 | party | `mu` | 2 | pass | `gy` | 2 |
| passage | `cll` | 3 | passenger | `clm` | 3 | passion | `cln` | 3 |
| password | `fwm` | 3 | past | `uj` | 2 | patch | `fwn` | 3 |
| path | `oy` | 2 | patience | `clp` | 3 | patient | `clq` | 3 |
| pattern | `clr` | 3 | pay | `fk` | 2 | payment | `cls` | 3 |
| peace | `clt` | 3 | peak | `clv` | 3 | penalty | `clw` | 3 |
| pension | `clx` | 3 | people | `jw` | 2 | percentage | `clz` | 3 |
| perception | `cmb` | 3 | perfect | `dxj` | 3 | perfectly | `fmj` | 3 |
| perform | `bbb` | 3 | performance | `cmc` | 3 | perhaps | `dh` | 2 |
| period | `cmd` | 3 | permanent | `dxk` | 3 | permanently | `fmk` | 3 |
| permission | `cmf` | 3 | person | `mq` | 2 | personal | `ra` | 2 |
| personality | `cmg` | 3 | personally | `fml` | 3 | perspective | `cmh` | 3 |
| phase | `cmj` | 3 | philosophy | `cmk` | 3 | phone | `cml` | 3 |
| photo | `cmm` | 3 | phrase | `cmn` | 3 | physical | `dxl` | 3 |
| physically | `fmm` | 3 | pick | `bbc` | 3 | picture | `cmp` | 3 |
| piece | `cmq` | 3 | pilot | `cmr` | 3 | pink | `dxm` | 3 |
| pipe | `cms` | 3 | pipeline | `fwp` | 3 | pitch | `cmt` | 3 |
| place | `kg` | 2 | plain | `dxn` | 3 | plan | `ja` | 2 |
| plane | `cmv` | 3 | plant | `cmw` | 3 | plastic | `dxp` | 3 |
| plate | `cmx` | 3 | platform | `cmz` | 3 | play | `ez` | 2 |
| player | `cnb` | 3 | pleasant | `dxq` | 3 | please | `vl` | 2 |
| pleased | `dxr` | 3 | pleasure | `cnc` | 3 | plenty | `cnd` | 3 |
| plugin | `fwq` | 3 | pocket | `cnf` | 3 | poem | `cng` | 3 |
| poet | `cnh` | 3 | poetry | `cnj` | 3 | point | `kr` | 2 |
| pointer | `fwr` | 3 | police | `cnk` | 3 | policy | `cnl` | 3 |
| political | `dxs` | 3 | politics | `cnm` | 3 | pollution | `cnn` | 3 |
| pool | `cnp` | 3 | poor | `dxt` | 3 | popular | `dxv` | 3 |
| population | `cnq` | 3 | port | `cnr` | 3 | position | `cns` | 3 |
| positive | `dxw` | 3 | possession | `cnt` | 3 | possibility | `cnv` | 3 |
| possible | `qv` | 2 | possibly | `fmn` | 3 | potential | `cnw` | 3 |
| potentially | `fmp` | 3 | pound | `cnx` | 3 | pour | `bbd` | 3 |
| poverty | `cnz` | 3 | power | `ls` | 2 | powerful | `dxx` | 3 |
| practical | `dxz` | 3 | practically | `fmq` | 3 | practice | `bbf` | 3 |
| prayer | `cpb` | 3 | precious | `dzb` | 3 | precisely | `fmr` | 3 |
| prefer | `bbg` | 3 | preference | `cpc` | 3 | prepare | `jl` | 2 |
| presence | `cpd` | 3 | present | `jn` | 2 | president | `cpf` | 3 |
| press | `bbh` | 3 | pressure | `cpg` | 3 | prevent | `bbj` | 3 |
| previous | `dzc` | 3 | previously | `fms` | 3 | price | `cph` | 3 |
| pride | `cpj` | 3 | priest | `cpk` | 3 | primarily | `fmt` | 3 |
| primary | `dzd` | 3 | prime | `dzf` | 3 | prince | `cpl` | 3 |
| princess | `cpm` | 3 | principal | `dzg` | 3 | principle | `cpn` | 3 |
| prior | `dzh` | 3 | priority | `cpp` | 3 | prison | `cpq` | 3 |
| prisoner | `cpr` | 3 | privacy | `cps` | 3 | private | `dzj` | 3 |
| privately | `fmv` | 3 | prize | `cpt` | 3 | probable | `dzk` | 3 |
| probably | `vi` | 2 | problem | `nj` | 2 | procedure | `cpv` | 3 |
| process | `og` | 2 | produce | `hg` | 2 | producer | `cpw` | 3 |
| product | `cpx` | 3 | production | `cpz` | 3 | profession | `cqb` | 3 |
| professional | `dzl` | 3 | professor | `cqc` | 3 | profile | `fws` | 3 |
| profit | `cqd` | 3 | program | `kl` | 2 | progress | `cqf` | 3 |
| project | `cqg` | 3 | promise | `bbk` | 3 | promotion | `cqh` | 3 |
| prompt | `fwt` | 3 | proof | `cqj` | 3 | proper | `dzm` | 3 |
| properly | `fmw` | 3 | property | `cqk` | 3 | proportion | `cql` | 3 |
| proposal | `cqm` | 3 | protect | `bbl` | 3 | protection | `cqn` | 3 |
| protest | `cqp` | 3 | protocol | `fwv` | 3 | proud | `dzn` | 3 |
| prove | `bbm` | 3 | provide | `hy` | 2 | provision | `cqq` | 3 |
| proxy | `fww` | 3 | psychological | `dzp` | 3 | pub | `cqr` | 3 |
| public | `qh` | 2 | publish | `bbn` | 3 | pull | `hd` | 2 |
| pure | `dzq` | 3 | purely | `fmx` | 3 | purple | `dzr` | 3 |
| purpose | `cqs` | 3 | push | `bbp` | 3 | put | `hs` | 2 |
| quality | `cqt` | 3 | quarter | `cqv` | 3 | queen | `cqw` | 3 |
| query | `fwx` | 3 | question | `km` | 2 | queue | `fwz` | 3 |
| quick | `dzs` | 3 | quickly | `fmz` | 3 | quiet | `dzt` | 3 |
| quietly | `fnb` | 3 | quite | `vd` | 2 | race | `cqx` | 3 |
| radical | `dzv` | 3 | rain | `cqz` | 3 | raise | `gx` | 2 |
| random | `dzw` | 3 | range | `crb` | 3 | rank | `crc` | 3 |
| rapid | `dzx` | 3 | rapidly | `fnc` | 3 | rare | `dzz` | 3 |
| rarely | `fnd` | 3 | rate | `crd` | 3 | rather | `ve` | 2 |
| ratio | `crf` | 3 | raw | `fbb` | 3 | reach | `gt` | 2 |
| reaction | `crg` | 3 | read | `fx` | 2 | reader | `crh` | 3 |
| readily | `fnf` | 3 | ready | `rp` | 2 | real | `qr` | 2 |
| realistic | `fbc` | 3 | reality | `crj` | 3 | realize | `bbq` | 3 |
| really | `vk` | 2 | reason | `mz` | 2 | reasonable | `fbd` | 3 |
| receive | `ia` | 2 | recent | `sc` | 2 | recently | `fng` | 3 |
| recession | `crk` | 3 | recognize | `bbr` | 3 | record | `jk` | 2 |
| recovery | `crl` | 3 | recursive | `fxb` | 3 | red | `rw` | 2 |
| reduce | `bbs` | 3 | reduction | `crm` | 3 | refactor | `fxc` | 3 |
| refer | `bbt` | 3 | reference | `crn` | 3 | reflect | `bbv` | 3 |
| reflection | `crp` | 3 | reform | `crq` | 3 | refuse | `bbw` | 3 |
| regard | `bbx` | 3 | regex | `fxd` | 3 | region | `crr` | 3 |
| register | `crs` | 3 | registry | `fxf` | 3 | regular | `fbf` | 3 |
| regularly | `fnh` | 3 | regulation | `crt` | 3 | relate | `bbz` | 3 |
| related | `fbg` | 3 | relation | `crv` | 3 | relationship | `crw` | 3 |
| relative | `fbh` | 3 | relatively | `fnj` | 3 | release | `bcb` | 3 |
| relevant | `fbj` | 3 | relief | `crx` | 3 | religion | `crz` | 3 |
| religious | `fbk` | 3 | reluctant | `fbl` | 3 | remain | `gv` | 2 |
| remaining | `fbm` | 3 | remarkable | `fbn` | 3 | remember | `gf` | 2 |
| remote | `fbp` | 3 | remove | `bcc` | 3 | render | `fxg` | 3 |
| repeat | `bcd` | 3 | repeatedly | `fnk` | 3 | replace | `jr` | 2 |
| replacement | `csb` | 3 | reply | `bcf` | 3 | report | `nr` | 2 |
| reporter | `csc` | 3 | repository | `fxh` | 3 | represent | `bcg` | 3 |
| representation | `csd` | 3 | representative | `fbq` | 3 | republic | `csf` | 3 |
| reputation | `csg` | 3 | request | `csh` | 3 | require | `hb` | 2 |
| requirement | `csj` | 3 | research | `na` | 2 | resident | `csk` | 3 |
| resolution | `csl` | 3 | resource | `csm` | 3 | respect | `csn` | 3 |
| respond | `bch` | 3 | response | `csp` | 3 | responsibility | `csq` | 3 |
| responsible | `fbr` | 3 | rest | `bcj` | 3 | restaurant | `csr` | 3 |
| result | `mv` | 2 | return | `jc` | 2 | reveal | `bck` | 3 |
| revenue | `css` | 3 | review | `cst` | 3 | revolution | `csv` | 3 |
| reward | `csw` | 3 | rice | `csx` | 3 | rich | `fbs` | 3 |
| right | `ql` | 2 | ring | `bcl` | 3 | rise | `bcm` | 3 |
| rising | `fbt` | 3 | risk | `csz` | 3 | river | `ctb` | 3 |
| road | `ctc` | 3 | rock | `ctd` | 3 | role | `ctf` | 3 |
| roll | `bcn` | 3 | roof | `ctg` | 3 | room | `ku` | 2 |
| root | `cth` | 3 | rope | `ctj` | 3 | rough | `fbv` | 3 |
| roughly | `fnl` | 3 | round | `ctk` | 3 | route | `ctl` | 3 |
| router | `fxj` | 3 | row | `ctm` | 3 | royal | `fbw` | 3 |
| rule | `ctn` | 3 | run | `fa` | 2 | runtime | `fxk` | 3 |
| rural | `fbx` | 3 | rush | `ctp` | 3 | sad | `fbz` | 3 |
| sadly | `fnm` | 3 | safe | `fcb` | 3 | safety | `ctq` | 3 |
| salary | `ctr` | 3 | sale | `cts` | 3 | salt | `ctt` | 3 |
| sample | `ctv` | 3 | sand | `ctw` | 3 | satisfaction | `ctx` | 3 |
| satisfied | `fcc` | 3 | save | `ig` | 2 | savings | `ctz` | 3 |
| say | `b` | 1 | scale | `cvb` | 3 | scared | `fcd` | 3 |
| scene | `cvc` | 3 | schedule | `cvd` | 3 | schema | `fxl` | 3 |
| scheme | `cvf` | 3 | school | `nn` | 2 | science | `cvg` | 3 |
| scientific | `fcf` | 3 | scientist | `cvh` | 3 | scope | `cvj` | 3 |
| score | `cvk` | 3 | screen | `cvl` | 3 | script | `fxm` | 3 |
| sea | `cvm` | 3 | search | `bcp` | 3 | season | `cvn` | 3 |
| seat | `cvp` | 3 | second | `frl` | 3 | secret | `fcg` | 3 |
| section | `cvq` | 3 | sector | `cvr` | 3 | secure | `fch` | 3 |
| security | `cvs` | 3 | see | `ee` | 2 | seek | `bcq` | 3 |
| seem | `el` | 2 | selection | `cvt` | 3 | selector | `fxn` | 3 |
| self/I | `c` | 1 | sell | `gz` | 2 | send | `gm` | 2 |
| senior | `fcj` | 3 | sense | `cvv` | 3 | sensitive | `fck` | 3 |
| sentence | `cvw` | 3 | separate | `bcr` | 3 | sequence | `cvx` | 3 |
| series | `cvz` | 3 | serious | `fcl` | 3 | seriously | `fnn` | 3 |
| servant | `cwb` | 3 | serve | `gk` | 2 | server | `pj` | 2 |
| service | `lp` | 2 | session | `cwc` | 3 | set | `fo` | 2 |
| setting | `cwd` | 3 | settle | `bcs` | 3 | seven | `fqr` | 3 |
| several | `sj` | 2 | severe | `fcm` | 3 | sex | `cwf` | 3 |
| sexual | `fcn` | 3 | shadow | `cwg` | 3 | shake | `bct` | 3 |
| shall | `uw` | 2 | shame | `cwh` | 3 | shape | `bcv` | 3 |
| share | `ij` | 2 | sharp | `fcp` | 3 | sharply | `fnp` | 3 |
| she | `af` | 2 | sheet | `cwj` | 3 | shelf | `cwk` | 3 |
| shell | `cwl` | 3 | shift | `cwm` | 3 | ship | `cwn` | 3 |
| shirt | `cwp` | 3 | shock | `cwq` | 3 | shoe | `cwr` | 3 |
| shoot | `jh` | 2 | shop | `cws` | 3 | short | `qy` | 2 |
| shot | `cwt` | 3 | should | `bh` | 2 | shoulder | `cwv` | 3 |
| shout | `bcw` | 3 | show | `ew` | 2 | shower | `cww` | 3 |
| shut | `bcx` | 3 | sick | `fcq` | 3 | side | `lk` | 2 |
| sight | `cwx` | 3 | sign | `cwz` | 3 | signal | `cxb` | 3 |
| significant | `fcr` | 3 | significantly | `fnq` | 3 | silence | `cxc` | 3 |
| silly | `fcs` | 3 | silver | `cxd` | 3 | similar | `fct` | 3 |
| simple | `rm` | 2 | simply | `fnr` | 3 | sin | `cxf` | 3 |
| since | `dc` | 2 | sing | `bcz` | 3 | singer | `cxg` | 3 |
| single | `qz` | 2 | sir | `cxh` | 3 | sister | `cxj` | 3 |
| sit | `fh` | 2 | site | `cxk` | 3 | situation | `cxl` | 3 |
| six | `fqq` | 3 | size | `cxm` | 3 | skill | `cxn` | 3 |
| skin | `cxp` | 3 | sky | `cxq` | 3 | sleep | `bdb` | 3 |
| slight | `fcv` | 3 | slightly | `fns` | 3 | slow | `rl` | 2 |
| slowly | `fnt` | 3 | small | `qb` | 2 | smart | `fcw` | 3 |
| smile | `bdc` | 3 | smooth | `fcx` | 3 | smoothly | `fnv` | 3 |
| snow | `cxr` | 3 | so | `ch` | 2 | social | `fcz` | 3 |
| society | `cxs` | 3 | socket | `fxp` | 3 | soft | `fdb` | 3 |
| softly | `fnw` | 3 | software | `cxt` | 3 | soil | `cxv` | 3 |
| soldier | `cxw` | 3 | solely | `fnx` | 3 | solid | `fdc` | 3 |
| solution | `cxx` | 3 | some | `ay` | 2 | somebody | `st` | 2 |
| somehow | `fnz` | 3 | someone | `dx` | 2 | something | `du` | 2 |
| sometimes | `va` | 2 | somewhat | `fpb` | 3 | son | `cxz` | 3 |
| song | `czb` | 3 | soon | `fpc` | 3 | sorry | `fdd` | 3 |
| sort | `ih` | 2 | soul | `czc` | 3 | sound | `ii` | 2 |
| source | `pd` | 2 | south | `czd` | 3 | southern | `fdf` | 3 |
| space | `czf` | 3 | spare | `fdg` | 3 | speak | `fw` | 2 |
| speaker | `czg` | 3 | special | `qx` | 2 | specific | `fdh` | 3 |
| specifically | `fpd` | 3 | speech | `czh` | 3 | speed | `czj` | 3 |
| spend | `ga` | 2 | spirit | `czk` | 3 | spiritual | `fdj` | 3 |
| sport | `czl` | 3 | spot | `czm` | 3 | spread | `bdd` | 3 |
| spring | `czn` | 3 | square | `czp` | 3 | stable | `fdk` | 3 |
| stack | `fxq` | 3 | staff | `czq` | 3 | stage | `czr` | 3 |
| stair | `czs` | 3 | stake | `czt` | 3 | stand | `fi` | 2 |
| standard | `czv` | 3 | star | `czw` | 3 | start | `hp` | 2 |
| state | `nl` | 2 | statement | `czx` | 3 | station | `czz` | 3 |
| status | `pk` | 2 | stay | `gq` | 2 | steadily | `fpf` | 3 |
| steady | `fdl` | 3 | steal | `bdf` | 3 | steep | `fdm` | 3 |
| step | `dbb` | 3 | stick | `bdg` | 3 | still | `ci` | 2 |
| stock | `dbc` | 3 | stomach | `dbd` | 3 | stone | `dbf` | 3 |
| stop | `fu` | 2 | storage | `fxr` | 3 | store | `dbg` | 3 |
| storm | `dbh` | 3 | story | `ky` | 2 | straight | `fdn` | 3 |
| strange | `fdp` | 3 | stranger | `dbj` | 3 | strategy | `dbk` | 3 |
| stream | `dbl` | 3 | street | `dbm` | 3 | strength | `dbn` | 3 |
| stress | `dbp` | 3 | stretch | `dbq` | 3 | strict | `fdq` | 3 |
| strike | `jp` | 2 | string | `os` | 2 | strong | `rn` | 2 |
| strongly | `fpg` | 3 | struct | `fxs` | 3 | structure | `dbr` | 3 |
| struggle | `dbs` | 3 | student | `dbt` | 3 | study | `ld` | 2 |
| stuff | `dbv` | 3 | stupid | `fdr` | 3 | style | `dbw` | 3 |
| subject | `dbx` | 3 | subsequently | `fph` | 3 | substantial | `fds` | 3 |
| succeed | `bdh` | 3 | success | `dbz` | 3 | successful | `fdt` | 3 |
| successfully | `fpj` | 3 | such | `sk` | 2 | sudden | `fdv` | 3 |
| suddenly | `fpk` | 3 | suffer | `bdj` | 3 | sufficient | `fdw` | 3 |
| sufficiently | `fpl` | 3 | sugar | `dcb` | 3 | suggest | `gw` | 2 |
| suggestion | `dcc` | 3 | suit | `dcd` | 3 | suitable | `fdx` | 3 |
| summer | `dcf` | 3 | sun | `dcg` | 3 | super | `fdz` | 3 |
| supply | `dch` | 3 | support | `iz` | 2 | suppose | `bdk` | 3 |
| sure | `qq` | 2 | surely | `fpm` | 3 | surface | `dcj` | 3 |
| surprise | `dck` | 3 | surprised | `ffb` | 3 | survey | `dcl` | 3 |
| survive | `bdl` | 3 | suspect | `dcm` | 3 | sweet | `dcn` | 3 |
| swimming | `dcp` | 3 | switch | `bdm` | 3 | symbol | `dcq` | 3 |
| sympathy | `dcr` | 3 | syntax | `fxt` | 3 | system | `kk` | 2 |
| table | `pc` | 2 | take | `ec` | 2 | tale | `dcs` | 3 |
| talent | `dct` | 3 | talk | `bdn` | 3 | tall | `ffc` | 3 |
| tank | `dcv` | 3 | target | `dcw` | 3 | task | `oc` | 2 |
| taste | `dcx` | 3 | tax | `dcz` | 3 | tea | `ddb` | 3 |
| teach | `bdp` | 3 | teacher | `nf` | 2 | teaching | `ddc` | 3 |
| team | `md` | 2 | tear | `ddd` | 3 | technically | `fpn` | 3 |
| technique | `ddf` | 3 | technology | `ddg` | 3 | telephone | `ddh` | 3 |
| television | `ddj` | 3 | tell | `ej` | 2 | temperature | `ddk` | 3 |
| template | `fxv` | 3 | temporarily | `fpp` | 3 | temporary | `ffd` | 3 |
| ten | `fqv` | 3 | tend | `bdq` | 3 | tendency | `ddl` | 3 |
| tension | `ddm` | 3 | term | `ddn` | 3 | terminal | `fxw` | 3 |
| terrible | `fff` | 3 | territory | `ddp` | 3 | terror | `ddq` | 3 |
| test | `oi` | 2 | text | `ddr` | 3 | than | `bt` | 2 |
| thank | `bdr` | 3 | thanks | `dds` | 3 | that | `ac` | 2 |
| the | `aa` | 2 | theater | `ddt` | 3 | their | `aq` | 2 |
| them | `ak` | 2 | theme | `ddv` | 3 | themselves | `ea` | 2 |
| then | `bz` | 2 | theory | `ddw` | 3 | there | `bb` | 2 |
| thereby | `fpq` | 3 | therefore | `ti` | 2 | these | `dr` | 2 |
| they | `ag` | 2 | thick | `ffg` | 3 | thin | `ffh` | 3 |
| thing | `nv` | 2 | think | `hm` | 2 | third | `frm` | 3 |
| thirty | `frb` | 3 | this | `f` | 1 | thoroughly | `fpr` | 3 |
| those | `ds` | 2 | though | `df` | 2 | thought | `ddx` | 3 |
| thousand | `frf` | 3 | thread | `fxx` | 3 | threat | `ddz` | 3 |
| three | `fqm` | 3 | throat | `dfb` | 3 | through | `cx` | 2 |
| throughout | `uk` | 2 | throw | `bds` | 3 | thus | `fps` | 3 |
| ticket | `dfc` | 3 | tie | `dfd` | 3 | till | `dff` | 3 |
| time | `jv` | 2 | timeout | `fxz` | 3 | tiny | `ffj` | 3 |
| tip | `dfg` | 3 | tired | `ffk` | 3 | title | `dfh` | 3 |
| to | `n` | 1 | today | `dfj` | 3 | toe | `dfk` | 3 |
| together | `fpt` | 3 | token | `pl` | 2 | tomorrow | `dfl` | 3 |
| tone | `dfm` | 3 | tongue | `dfn` | 3 | tonight | `dfp` | 3 |
| too | `cg` | 2 | tool | `ph` | 2 | tooth | `dfq` | 3 |
| top | `dfr` | 3 | topic | `dfs` | 3 | total | `dft` | 3 |
| totally | `fpv` | 3 | touch | `hz` | 2 | tough | `ffl` | 3 |
| tour | `dfv` | 3 | tourist | `dfw` | 3 | toward | `ul` | 2 |
| towards | `uo` | 2 | tower | `dfx` | 3 | town | `dfz` | 3 |
| trace | `fzb` | 3 | track | `dgb` | 3 | trade | `dgc` | 3 |
| tradition | `dgd` | 3 | traditional | `ffm` | 3 | traffic | `dgf` | 3 |
| train | `jb` | 2 | training | `dgg` | 3 | transition | `dgh` | 3 |
| transport | `dgj` | 3 | travel | `bdt` | 3 | treat | `bdv` | 3 |
| treatment | `dgk` | 3 | tree | `dgl` | 3 | tremendous | `ffn` | 3 |
| trend | `dgm` | 3 | trial | `dgn` | 3 | trick | `dgp` | 3 |
| trigger | `fzc` | 3 | trip | `dgq` | 3 | triple | `frj` | 3 |
| troop | `dgs` | 3 | tropical | `ffp` | 3 | trouble | `dgr` | 3 |
| true | `1` | 1 | truly | `fpw` | 3 | trust | `dgt` | 3 |
| truth | `dgv` | 3 | try | `ep` | 2 | turn | `hq` | 2 |
| twelve | `fqx` | 3 | twenty | `fqz` | 3 | twice | `fpx` | 3 |
| two | `fql` | 3 | type | `ol` | 2 | typical | `ffq` | 3 |
| typically | `fpz` | 3 | ugly | `ffr` | 3 | ultimately | `fqb` | 3 |
| unable | `ffs` | 3 | uncertain | `fft` | 3 | uncle | `dgw` | 3 |
| uncomfortable | `ffv` | 3 | under | `cz` | 2 | underneath | `uq` | 2 |
| understand | `fr` | 2 | unfortunately | `fqc` | 3 | union | `dgx` | 3 |
| unique | `ffw` | 3 | unit | `dgz` | 3 | united | `ffx` | 3 |
| university | `dhb` | 3 | unless | `tc` | 2 | unlikely | `ffz` | 3 |
| until | `da` | 2 | unusual | `fgb` | 3 | up | `cw` | 2 |
| upload | `fzd` | 3 | upon | `ur` | 2 | upper | `fgc` | 3 |
| upset | `fgd` | 3 | urban | `fgf` | 3 | url | `fzf` | 3 |
| use | `eg` | 2 | useful | `fgg` | 3 | user | `oj` | 2 |
| usual | `fgh` | 3 | usually | `fqd` | 3 | utility | `fzg` | 3 |
| utterly | `fqf` | 3 | validate | `fzh` | 3 | valley | `dhc` | 3 |
| valuable | `fgj` | 3 | value | `om` | 2 | variable | `fzj` | 3 |
| variation | `dhd` | 3 | variety | `dhf` | 3 | various | `fgk` | 3 |
| vast | `fgl` | 3 | vector | `fzk` | 3 | vehicle | `dhg` | 3 |
| version | `dhh` | 3 | very | `cd` | 2 | victim | `dhj` | 3 |
| victory | `dhk` | 3 | view | `dhl` | 3 | village | `dhm` | 3 |
| violence | `dhn` | 3 | violent | `fgm` | 3 | virtual | `fzl` | 3 |
| virtually | `fqg` | 3 | visible | `fgn` | 3 | vision | `dhp` | 3 |
| visit | `bdw` | 3 | visitor | `dhq` | 3 | visual | `fgp` | 3 |
| vital | `fgq` | 3 | voice | `dhr` | 3 | volume | `dhs` | 3 |
| vote | `bdx` | 3 | wage | `dht` | 3 | wait | `gj` | 2 |
| wake | `bdz` | 3 | walk | `gc` | 2 | wall | `dhv` | 3 |
| want | `ef` | 2 | war | `ms` | 2 | warm | `fgr` | 3 |
| warn | `bfb` | 3 | warning | `dhw` | 3 | was | `bi` | 2 |
| wash | `bfc` | 3 | waste | `dhx` | 3 | watch | `fs` | 2 |
| water | `kt` | 2 | wave | `dhz` | 3 | way | `jx` | 2 |
| we | `u` | 1 | weak | `fgs` | 3 | weakness | `djb` | 3 |
| wealth | `djc` | 3 | wealthy | `fgt` | 3 | weapon | `djd` | 3 |
| wear | `bfd` | 3 | weather | `djf` | 3 | website | `djg` | 3 |
| wedding | `djh` | 3 | week | `ki` | 2 | weekend | `djj` | 3 |
| weight | `djk` | 3 | weird | `fgv` | 3 | welcome | `fgw` | 3 |
| welfare | `djl` | 3 | were | `bj` | 2 | west | `djm` | 3 |
| western | `fgx` | 3 | wet | `fgz` | 3 | what | `g` | 1 |
| wheel | `djn` | 3 | when | `bv` | 2 | whenever | `tf` | 2 |
| where | `bw` | 2 | whereas | `tb` | 2 | wherever | `tg` | 2 |
| whether | `te` | 2 | which | `au` | 2 | while | `db` | 2 |
| white | `rv` | 2 | who | `ar` | 2 | whole | `qw` | 2 |
| whom | `sm` | 2 | whose | `sn` | 2 | wide | `fhb` | 3 |
| widely | `fqh` | 3 | widget | `fzm` | 3 | wife | `djp` | 3 |
| wild | `fhc` | 3 | will | `bc` | 2 | willing | `fhd` | 3 |
| win | `gd` | 2 | wind | `djq` | 3 | window | `djr` | 3 |
| wine | `djs` | 3 | wing | `djt` | 3 | winner | `djv` | 3 |
| winter | `djw` | 3 | wise | `fhf` | 3 | wish | `iy` | 2 |
| with | `d` | 1 | within | `ut` | 2 | without | `uu` | 2 |
| witness | `djx` | 3 | woman | `ka` | 2 | wonder | `bff` | 3 |
| wonderful | `fhg` | 3 | wood | `djz` | 3 | wooden | `fhh` | 3 |
| word | `lh` | 2 | work | `kn` | 2 | worker | `dkb` | 3 |
| world | `kc` | 2 | worry | `bfg` | 3 | worth | `fhj` | 3 |
| would | `ba` | 2 | write | `fg` | 2 | writing | `dkc` | 3 |
| wrong | `fhk` | 3 | xml | `fzn` | 3 | yaml | `fzp` | 3 |
| yard | `dkd` | 3 | year | `nt` | 2 | yellow | `fhl` | 3 |
| yes | `vm` | 2 | yesterday | `fqj` | 3 | yet | `dg` | 2 |
| you | `z` | 1 | young | `qf` | 2 | yourself | `sw` | 2 |
| youth | `dkf` | 3 | zero | `fqk` | 3 | zone | `dkg` | 3 |

---

## 5. Operations

Structured agent commands use S-expression syntax: `(verb arg ...)`.

### 5.1 Format
```
(verb arg1 arg2 ...)
```
Arguments: tokens, literals, or nested operations.

### 5.2 Core Operations

**File I/O:**
```
(fx <ref>)                     — read
(fg <ref> <line> <content>)    — write at line
(ei <pattern> v <scope>)       — find in scope
(jt <ref>)                     — delete
(ix <ref> <ref>)               — copy
(fb <ref> <ref>)               — move
```

**Execution:**
```
(fa <ref>)                      — run
(oi <ref>)                     — test
(ftb <target>)                  — deploy
(es <ref> <args>)              — call/invoke
```

**Control Flow:**
```
(cvx <op1> <op2> ...)          — sequence
(fwb <count> <op>)               — loop N times
(fwb 9 <ref> <op>)               — loop each item
```

**Communication:**
```
(gm <content> n <dest>)        — send to
(ia 2 <source>)               — receive from
```

**Conditional:**
```
q <condition> bz <then-clause> tn <else-clause>
```

---

## 6. Reference System

Bind labels with `->` for reuse. References = word + digits.

### 6.1 Binding
```
nz1 -> "/src/app.py"
oa1 -> "validate_input"
```

### 6.2 Usage
```
nz1 -> "/src/app.py"
nz2 -> "/src/utils.py"
(fx nz1)
(ei "def validate" v nz2)
(fg nz1 3 "import validate")
```

References are valid from binding to end of message.

---

## 7. Patterns

### Pattern 1 — Read-Modify-Write
```
(cvx (fx <ref>)(fg <ref> <line> <content>)(hw <ref>))
```

### Pattern 2 — Search and Act
```
mv1 -> (ei <pattern> v <scope>)
(fwb 9 mv1 (<op>))
```

### Pattern 3 — Conditional
```
q <condition> bz <then> tn <else>
```

### Pattern 4 — Error Guard
```
(ep <op>) q ob bz (ju ob) tn (fu)
```

### Pattern 5 — Task Delegation
```
(gm oc1 n pm1)
(gj mv 2 pm1)
```

### Pattern 6 — Pipeline
```
mv1 -> (<op1>)
mv2 -> (<op2> mv1)
mv3 -> (<op3> mv2)
```

---

## 8. Semantic Composition

The vocabulary maps common words 1:1. For concepts **outside** the vocabulary,
compose meaning from ~100 semantic primitives instead of falling back to quoted English.

### 8.1 Concept Composition — `:` operator

Combines concepts. Head concept first, modifiers after.

| Composition | Expansion | English meaning |
|-------------|-----------|-----------------|
| `bvw:dxm` | flower:pink | pink flower |
| `bvw:dxm:py` | flower:pink:big | big pink flower (peony) |
| `kt:ng:tr` | water:force:above | geyser |
| `ee:s:mh` | see:not:body | ghost / specter |
| `im:dm:qb` | design:many:small | ornate |
| `bvq:qb` | fire:small | candle / ember |
| `kt:py:ng` | water:big:force | tsunami / flood |
| `dbf:rg:brn` | stone:hot:earth | volcano |
| `ne:ng:rk` | air:force:fast | storm / hurricane |
| `rj:dm:qb` | light:many:small | glitter / sparkle |
| `kt:rh:rv` | water:cold:white | snow / ice |
| `bwt:lf` | glass:eye | lens / spectacle |
| `bvq:rj:tr` | fire:light:above | beacon / lighthouse |
| `djz:kt:fb` | wood:water:move | boat / raft |
| `cgt:rg:rw` | metal:hot:red | forge / molten metal |
| `bvw:rv:qb` | flower:white:small | daisy |
| `bvw:rw:nx` | flower:red:love | rose |
| `brn:ry:dm` | earth:green:many | meadow / field |
| `ml:pq:nx` | face:good:love | beauty / adoration |
| `ke:im:qb` | hand:design:small | craft / artisan work |
| `lf:dqz` | eye:far | telescope / binoculars |
| `kt:ry:gb` | water:green:grow | swamp / marsh |
| `dbf:qk:py` | stone:old:big | monument / ruin |
| `ne:rh:rv` | air:cold:white | fog / mist |
| `rj:dm:tr` | light:many:above | stars / constellation |

**Parser rule:** `p.` and `f.` at token start = tense prefix. All `:` within a token = composition.

### 8.2 Semantic Primitives

~97 root concepts from the vocabulary, tagged as composable building blocks:

| Domain | Count | Examples |
|--------|-------|---------|
| Physical properties | 20 | big/`py`, small/`qb`, hot/`rg`, cold/`rh`, fast/`rk`, slow/`rl`, hard/`qu`, soft/`fdb`, heavy/`dss`, light/`rj`, long/`pu`, short/`qy`, wide/`fhb`, thin/`ffh`, deep/`dns`, flat/`drh`, round/`ctk`, sharp/`fcp`, smooth/`fcx`, rough/`fbv` |
| Colors | 8 | red/`rw`, blue/`rx`, green/`ry`, pink/`dxm`, black/`ru`, white/`rv`, yellow/`fhl`, brown/`dmb` |
| Elements | 10 | water/`kt`, fire/`bvq`, air/`ne`, glass/`bwt`, stone/`dbf`, earth/`brn`, light/`rj`, wood/`djz`, metal/`cgt`, ice/`bzs` |
| Body | 8 | body/`mh`, face/`ml`, hand/`ke`, eye/`lf`, head/`lm`, arm/`bgk`, leg/`cdv`, mouth/`chr` |
| Core actions | 15 | move/`fb`, take/`ec`, break/`hk`, hold/`hl`, open/`rd`, close/`rf`, cut/`gs`, make/`i`, give/`6`, put/`hs`, build/`gp`, push/`bbp`, pull/`hd`, turn/`hq`, throw/`bds` |
| Perception | 10 | see/`ee`, hear/`ey`, feel/`eo`, think/`hm`, show/`ew`, speak/`fw`, touch/`hz`, watch/`fs`, know/`j`, believe/`fd` |
| States | 10 | good/`pq`, bad/`qi`, new/`pr`, live/`fc`, full/`qs`, dead/`dnp`, old/`qk`, strong/`rn`, weak/`fgs`, clean/`wm` |
| Spatial | 6 | above/`tr`, below/`ty`, near/`uf`, far/`dqz`, inside/`ue`, outside/`ui` |
| Quantity | 6 | one/`dt`, many/`dm`, few/`dp`, none/`ss`, all/`r`, some/`ay` |
| Social | 6 | love/`nx`, fear/`bvg`, help/`hn`, fight/`iu`, friend/`lq`, war/`ms` |
| Abstract | 10 | time/`jv`, place/`kg`, thing/`nv`, force/`ng`, power/`ls`, way/`jx`, cause/`il`, change/`mw`, end/`lw`, start/`hp` |

### 8.3 Intent Frames — `{}` syntax

Capture communicative purpose, not sentence structure.

**Syntax:** `{FRAME-TYPE [SUBJECT] CONTENT}`

- First token = intent type
- Optional second token = subject being framed
- Rest = semantic content using compositions and regular AGNTCL
- Frames can nest

**Intent types:**

| Intent | AGNTCL | Usage |
|--------|-----|-------|
| suggest | `gw` | `{gw ...}` — propose an action |
| describe | `je` | `{je ...}` — characterize something |
| ask | `ek` | `{ek ...}` — request information |
| explain | `xw` | `{xw ...}` — clarify reasoning |
| warn | `bfb` | `{bfb ...}` — flag risk or danger |
| compare | `wq` | `{wq ...}` — relate two things |
| cause | `il` | `{il ...}` — state causation |
| example | `btd` | `{btd ...}` — provide illustration |

**Example:**
```
EN:  I suggest we use a big pink flower as the design element
AGNTCL: {gw u eg bvw:dxm:py im}

EN:  Can you describe how the storm affected the garden?
AGNTCL: {ek {je ne:ng:rk p.mw bwn}}
```

### 8.4 Approximate Marker — `~` prefix

Signals a composition is a best-effort approximation, not an exact match.

| Expression | Meaning |
|------------|---------|
| `~bvw:dxm:py` | approximately a big pink flower (≈ peony) |
| `~ee:s:mh` | something like an invisible being (≈ specter) |
| `~dbf:rg:brn` | roughly a hot-earth-stone formation (≈ volcano) |

Agents encountering `~` know the composition is approximate — close but not exact.

### 8.5 Semantic vs Literal Guide

**Florist passage (English — 218 chars):**
> The ornate shop displayed peonies, roses, and daisies. A specter of beauty
> hung in the air. Each arrangement was a small masterpiece — flowers chosen
> for color and meaning, petals like stained glass catching the light.

**Literal mode** (word-for-word, quotes for out-of-vocab — 156 chars, 28% compression):
```
"ornate" cws p.ew "peonies" "roses" m "daisies"
"specter" t "beauty" p.yk v ne
9 bgm bi qb "masterpiece"
bvw p.ib l blt m cgj
"petals" o "stained" bwt wk rj
```
**9 quoted fallbacks:** `"ornate"`, `"peonies"`, `"roses"`, `"daisies"`, `"specter"`, `"beauty"`, `"masterpiece"`, `"petals"`, `"stained"` — these require both agents to know English.

**Semantic mode** (compositions + intent frame — 132 chars, 39% compression):
```
{je cws:im:dm:qb
  p.ew ~bvw:dxm:py ~bvw:rw:nx ~bvw:rv:qb
  ~ee:s:mh:dln p.yk:ne
  9 bgm qb ~im:pq:ke
  bvw p.ib:blt:cgj
  bvw:ffh bwt:blt:rj}
```
**Zero quoted words.** All 9 out-of-vocab concepts composed from primitives.

**Compression comparison:**

| Mode | Chars | Compression | Quoted fallbacks |
|------|-------|-------------|-----------------|
| English original | 218 | — | — |
| Literal AGNTCL | 156 | 28% | 9 (requires English) |
| Semantic AGNTCL | 132 | 39% | 0 (fully closed) |

The primary win is **vocabulary closure**: semantic mode eliminates all English
dependency. The extra ~11% compression is secondary to never needing quoted fallbacks.

---

## 9. Examples

### 9.1 Personal
```
EN:  My name is Tim and I like to play soccer
AGNTCL: y mc k "Tim" m c o ez "soccer"
```

### 9.2 File Operations
```
EN:  Read the file, edit line 42, then run the tests
AGNTCL: (cvx (fx nz1)(fg nz1 42 "return True")(fa oi1))
```

### 9.3 Uncertainty
```
EN:  I don't know if this will work but let's try
AGNTCL: c !j q f f.kn e ep
```

### 9.4 Task Assignment
```
EN:  Create a task for Alice to design the logo before we send
AGNTCL: (i oc l "Alice" im "logo" cq u gm)
```

### 9.5 Conditional Logic
```
EN:  If the tests pass, deploy to production. Otherwise send the error to the team.
AGNTCL: q oi k 1 bz (ftb "prod") tn (gm ob n md)
```

### 9.6 Search
```
EN:  Find all Python files in the source directory containing validate
AGNTCL: (ei "*.py" v "src" d "validate")
```

### 9.7 Error Handling
```
EN:  The build failed because of a missing dependency. Install it and retry.
AGNTCL: gp p.xz bu !h fsz (cvx (fvz x)(ep gp))
```

### 9.8 Multi-step Workflow
```
EN:  Clone the repo, checkout feature branch, read config, update timeout to 30, run tests.
AGNTCL: oy1 -> "repo_url"
     nz1 -> "config.yml"
     (cvx (ix oy1)(p "feature")(fx nz1)(fg nz1 "timeout" 30)(fa oi1))
```

### 9.9 Collaboration
```
EN:  We need Alice to review the code and Bob to write tests.
     If both agree, deploy. Otherwise, send me the feedback.
AGNTCL: u nw "Alice" n hw oa1 m "Bob" n fg oi
     q hu bz (ftb) tn (gm mv n c)
```

### 9.10 Temporal
```
EN:  The server was always fast before. Now it is slow.
     I think something changed after the last deploy.
AGNTCL: "srv" p.k cn rk cq ca x k rl
     c hm du p.mw cp pt ftb
```

---

## 10. Grammar Specification (BNF)

```bnf
<message>      ::= <statement> (" " <statement>)*

<statement>    ::= <operation>
               |   <frame>
               |   <binding>
               |   <expression>

<operation>    ::= "(" <token> (" " <argument>)* ")"

<frame>        ::= "{" <token> (" " <argument>)* "}"

<argument>     ::= <token>
               |   <operation>
               |   <frame>
               |   <literal>

<binding>      ::= <reference> " -> " <bind-value>

<bind-value>   ::= <literal>
               |   <operation>

<expression>   ::= <token> (" " <token>)*

<token>        ::= <prefix>* <word>

<prefix>       ::= "p." | "f." | "!" | "?" | "~"

<word>         ::= <tier1>
               |   <tier2>
               |   <tier3>
               |   <composition>
               |   <reference>

<composition>  ::= <word> (":" <word>)+

<tier1>        ::= [a-z] | [0-9]

<tier2>        ::= [a-z] [a-z]        /* excluding 54 English words */

<tier3>        ::= <consonant>{3}

<reference>    ::= <word> [0-9]+

<consonant>    ::= [bcdfghjklmnpqrstvwxz]

<literal>      ::= <string> | <number>

<string>       ::= '"' [^"]* '"'

<number>       ::= [0-9] [0-9]+        /* 2+ digits = literal */
```

### Reserved Syntax Characters

| Char | Purpose |
|------|---------|
| `( )` | Operation delimiters |
| `{ }` | Intent frame delimiters |
| `"` | String literal delimiters |
| `:` | Composition operator |
| `~` | Approximate marker prefix |
| `.` | Tense prefix separator |
| `!` | Negation prefix |
| `?` | Question prefix |
| `->` | Binding operator |
| ` ` | Token delimiter |