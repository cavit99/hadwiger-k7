# Adjacent degree-eight true-twin `C_7` checkpoint

**Status:** archived local research checkpoint recovered on 22 August 2026.
The files in this directory are not on the active proof spine and are not
promoted audited results.  They preserve the sound part of the adjacent
true-twin route together with the exact RED finding that stopped it.

The four principal notes were recovered byte-for-byte from the earlier
scratch workspace.  Their claim boundary is:

1. a hypothetical adjacent degree-eight true-twin boundary reduces to an
   induced `C_7`;
2. the exterior is three-connected and every portal set has order at most
   two or is a consecutive triple;
3. the portal profiles are arc-local; and
4. the attempted pure-`C_7` `st`-numbering completion is false.  Its verified
   repair gives

   ```text
   |N_T(x) union N_T(y)| <= 3
   ```

   for every exterior edge `xy`, and leaves 140 finite obstruction profiles
   belonging to an unbounded connected-support packing problem.

The earlier arc-local note still records the superseded upper bound four.
Read it together with `cold_audit_pure_c7_st_support_capstone.md`, which
proves the corrected cap three and records the RED verdict.  Do not cite the
false `st`-numbering capstone as a theorem.

The separate fixed-`C_5+K_2` `st`-numbering theorem is retained because the
induced-`C_7` reduction invokes its elementary interval lemmas.  Its GREEN
audit does not validate the false pure-`C_7` extension.

## Principal source hashes

```text
51a0f275efbfcf16a0de48c6ec065bfcf30b7db97d031eecd529817ae69e61c9  draft_adjacent_true_twins_c7_normal_form.md
fbff2c621f70b1390688b1a64420d765972bbe4bb595a98a2eb2fc2ec66d9fd7  pure_c7_portal_classification_and_disconnected_exterior.md
c8eb5da4e4dbbfdfe87e235063e5e0fd79f39bfaa86f3a0315f262ebcfbe25d3  pure_c7_arc_local_threeconnected_normal_form.md
4b861a6bd744c66458de6046ae61b540ef24e1db44bf03ac3b2a3321c05c86f9  cold_audit_pure_c7_st_support_capstone.md
```

## Reproduction

From this directory:

```bash
cc -O3 verify_adjacent_true_twins_c7_normal_form.c -o /tmp/c7-normal
/tmp/c7-normal

c++ -O3 verify_c7_twocut_fivebag_partition.cpp -o /tmp/c7-twocut
/tmp/c7-twocut

python3 verify_c7_twocut_restricted_orbits.py

cc -O3 verify_c7_two_support_anchored_k5minus.c -o /tmp/c7-two-support
/tmp/c7-two-support

cc -O3 verify_c7_support3_full_sevenbag.c -o /tmp/c7-support3
/tmp/c7-support3
```

The last program deliberately exits with status one after reporting
`union_full_support_pairs=1989 failures=140`; that nonzero exit is the
expected falsification certificate.  The independent three-shore diagnostic
similarly reports `profiles=9464 failures=518`.

The order-eight MILP experiment was not recovered into this bundle: it used
untracked SciPy dependencies and had no retained input/output log.  No claim
in this checkpoint depends on it.
